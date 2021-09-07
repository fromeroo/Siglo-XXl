<?php

namespace App\Http\Controllers\Intranet;

use App\Models\User;
use Illuminate\Http\Request;
use App\Http\Controllers\Controller;
use Illuminate\Support\Facades\Auth;
use Illuminate\Foundation\Auth\AuthenticatesUsers;
use Illuminate\Foundation\Auth\AuthenticatesHotels;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Facades\Mail;
use DB;

class AuthController extends Controller
{

    public function __construct()
    {
        //return $this->middleware('guest', ['only' => ['showLogin','showSendPassword','showRecoveryPassword']]);
    }

    public function x(){
        $cone = oci_connect('c##franco', 'password', 'SIGLO_XXL');

        $sql = oci_parse($cone, "SELECT * FROM BANCO");
        oci_execute($sql);
        while(oci_fetch($sql)) {
            $return = oci_result($sql, 'NOM_BCO');
        }
        dd($return);
    }

    public function login(Request $request)
    {
        // $this->validate($request, [
        //     'email' => 'required|string',
        //     'password' => 'required|string'
        // ]);

        // if (Auth::guard('intranet')->attempt(['email' => $request->email, 'password' => $request->password])) {
            
        //     if (auth()->guard('intranet')->user()->active == 1) {
        //         //session()->put('user_auth', auth('intranet')->user());
        //         if (auth()->guard('intranet')->user()->is_hotel == 1) {
        //             return redirect()->route('intranet.invitations.index');
        //         }
        //         return redirect()->route('intranet.dashboard');
                
        //     } else {
        //         return back()->withErrors(['error' => 'Su usuario se encuentra inactivo, comuníquese con un administrador del sistema para regularizar su situación.'])->withInput();
        //     }
        // }
        // return back()->withErrors(['error' => 'La combinación de email y contraseña es incorrecta.'])->withInput();
        if($request->email == 'fr.romeroo@duocuc.cl' && $request->password == 'admin123'){
            return redirect()->route('intranet.dashboard');
        }
        else
        {
            return back()->withErrors(['error' => 'La combinación de email y contraseña es incorrecta.'])->withInput();
        }
    }

    public function show()
    {
        if (auth()->guard('intranet')->user()) {
            return redirect()->intended(route('intranet.dashboard'));
        }
        return view('intranet.auth.show');
    }

    protected function guard()
    {
        return Auth::guard('guard-name');
    }

    public function sendPassword(Request $request)
    {
        $this->validate($request, [
            'email' => 'required|string',
        ]);

        $user = User::where('email', $request->email)->first();

        if ($user) {
            $user->remember_token = rand(1000, 9999);
            $user->save();

            $html = view('intranet.emails.send-password', ['nombre' => $user->first_name . ' ' . $user->last_name, 'texto' => 'Su código de recuperación de contraseña es: <b>' . $user->remember_token . '</b>.<br/><br/>Le saluda atentamente,<br/><br/>Administrador Inland.'])->render();

            $email = new \SendGrid\Mail\Mail();

            $email->setFrom('info@inland.cl', 'Inland'); //DESDE
            $email->setSubject('Código para restablecer contraseña'); //ASUNTO
            $email->addTo($user->email, $user->first_name . ' ' . $user->last_name); //HACIA
            $email->addContent(
                "text/html", $html
            );

            $sendgrid = new \SendGrid(env('SENDGRID_APP_KEY'));

            $response = $sendgrid->send($email);

            session()->flash('success', 'Le hemos enviado un correo electrónico con un código para restablecer su contraseña.');
            return redirect()->route('intranet.auth.show-recovery-password');
        }
        return back()->withErrors(['email' => 'El email ingresado no existe en nuestro sistema.'])->withInput();

    }

    public function showSendPassword()
    {
        return view('intranet.auth.send_password');
    }

    public function recoveryPassword(Request $request)
    {
        $this->validate($request, [
            'remember_token' => 'required|numeric|max:10000',
            'email' => 'required|string',
            'password' => 'required|min:4|confirmed',
            'password_confirmation' => 'required|min:4'
        ]);

        $user = User::where('email', $request->email)->first();

        if ($user) {

            if ($user->remember_token == $request->remember_token) {
                $user->password = bcrypt($request->password);
                $user->remember_token = null;
                $user->save();

                session()->flash('success', 'Se ha modificado correctamente su contraseña.');
                return redirect()->route('intranet.auth.show');

            }
            return back()->withErrors(['remember_token' => 'El código de recuperación no coincide con el enviado a su correo.'])->withInput();
        } else {
            return back()->withErrors(['rut' => 'El rut no existe en nuestra base de datos.'])->withInput();
        }

        return redirect()->route('intranet.auth.show-recovery-password');

    }

    public function showRecoveryPassword()
    {
        return view('intranet.auth.recovery_password');
    }

    public function logout()
    {
        Auth::guard('intranet')->logout();
        return redirect(route('intranet.dashboard'));
    }
}
