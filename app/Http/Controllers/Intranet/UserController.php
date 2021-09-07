<?php

namespace App\Http\Controllers\Intranet;

use App\Models\User;
use App\Models\Store;
use Illuminate\Http\Request;

use Illuminate\Support\Facades\Validator;
use Spatie\Permission\Models\Permission;
use Spatie\Permission\Models\Role;

class UserController extends GlobalController
{
    protected $options = [
        'route' => 'intranet.users.',
        'folder' => 'intranet.modules.users.',
        'pluralName' => 'Usuarios',
        'singularName' => 'Usuario',
        'addToBlade' => [
            'viewPermission' => 'Permisos del Usuario'
        ],
        'disableActions' => ['changeStatus', 'show'],
    ];


    public function __construct()
    {
        parent::__construct($this->options);
    }

    public function index()
    {

        $objects = User::orderBy('first_name')->with('roles')->get()->except(1);
        $active = User::where('active', 1)->count();
        if ($active > 0) {
            $name_button = 'Desactivar todos';
        } else {
            $name_button = 'Activar todos';
        }
        return view($this->folder . 'index', compact('objects', 'name_button'));
    }

    public function create()
    {
        $roles = Role::all()->except(1);
        return view($this->folder . 'create', compact('roles'));
    }

    public function store(Request $request)
    {
        $rules = [
            'email' => 'required|email:filter|regex:/(.*)@(.*)\.(.*)/i|unique:users,email',
            'password' => 'required|min:4|string',
            'first_name' => 'required',
            'last_name' => 'required',
            //'role_id' => 'required'
        ];

        $messages = [
            'email.unique' => 'El correo ingresado ya se encuentra registrado.'
            // 'role_id.required' => 'Debes seleccionar un rol para el usuario.',
        ];

        $validator = Validator::make($request->all(), $rules, $messages);

        if ($validator->passes()) {

            $object = User::create($request->all());
            $object->assignRole(1);
//            $object->assignRole($request->role_id);
            $object->password = bcrypt($request->password);
            $object->save();

            if ($object) {
                session()->flash('success', 'Usuario creado correctamente.');
                return redirect()->route($this->route . 'index');
            }

            return redirect()->back()->withErrors(['mensaje' => 'Error inesperado al crear el usuario.'])->withInput();
        } else {
            return redirect()->back()->withErrors($validator)->withInput();
        }
    }

    public function edit($id)
    {
        $object = User::with('roles')->find($id);
        $roles = Role::all()->except([1, 2001, 2002]);

        return view($this->folder . 'edit', compact('object', 'roles'));
    }

    public function update(Request $request, $id)
    {

        $object = User::find($id);

        if (!$object) {
            session()->flash('warning', 'Usuario no encontrado.');
            return redirect()->route($this->route . 'index');
        }
        if ($object->id == 1) {
            session()->flash('warning', 'Este usuario no puede ser modificado.');
            return redirect()->route($this->route . 'index');
        }

        $rules = [
            'email' => 'email:filter|regex:/(.*)@(.*)\.(.*)/i|unique:users,email,' . $id,
            'first_name' => 'required',
            'last_name' => 'required',
//            'role_id' => 'required'
        ];

        $messages = [
            'role_id.required' => 'Debes seleccionar un rol para el usuario.',
            'email.unique' => OutputMessage::FIELD_EMAIL_UNIQUE,
        ];

        $validator = Validator::make($request->all(), $rules, $messages);

        if ($validator->passes()) {

            $object->update($request->except('password', 'id'));
//            $object->syncRoles([]);
//            $object->syncRoles([$request->role_id]);
            if ($request->password) {
                $object->password = bcrypt($request->password);
            }
            $object->save();

            if ($object) {
                session()->flash('success', 'Usuario actualizado correctamente.');
                return redirect()->route($this->route . 'index');
            }
            return redirect()->back()->withErrors(['mensaje' => 'Error inesperado al modificar el usuario.'])->withInput();
        } else {
            return redirect()->back()->withErrors($validator)->withInput();
        }
    }

    public function destroy($id)
    {
        $object = User::find($id);

        if (!$object) {
            session()->flash('warning', 'Usuario no encontrado.');
            return redirect()->route($this->route . 'index');
        }

        if ($object->id == 1) {
            session()->flash('warning', 'Este usuario no puede ser eliminado.');
            return redirect()->route($this->route . 'index');
        }

        if ($object->delete()) {
            session()->flash('success', 'Usuario eliminado correctamente.');
            return redirect()->route($this->route . 'index');
        }
        session()->flash('error', 'No se ha podido eliminar el usuario.');
        return redirect()->route($this->route . 'index');
    }

    public function active(Request $request)
    {

        try {

            $object = User::find($request->id);

            if ($object) {

                $object->active = $request->active == 'true' ? 1 : 0;
                $object->save();

                return response()->json([
                    'status' => 'success',
                    'message' => $object->active == 1 ? 'Usuario activado correctamente.' : 'Usuario desactivado correctamente.',
                    'object' => $object
                ]);

            } else {

                return response()->json([
                    'status' => 'error',
                    'message' => 'Usuario no encontrado.'
                ]);
            }

        } catch (\Exception $e) {

            return response()->json([
                'status' => 'error',
                'message' => 'Ha ocurrido un error inesperado, inténtelo denuevo más tarde.' . $e->getMessage()
            ]);
        }

    }

    public function all_change(Request $request)
    {
        $active = User::where('active', 1)->count();
        if ($active > 0) {
            $users = User::get()->except(1);
            foreach ($users as $object) {
                $object->active = 0;
                $object->save();
            }
            session()->flash('success', 'Se han desactivado todos los usuarios.');
        } else {
            $users = User::get();
            foreach ($users as $object) {
                $object->active = 1;
                $object->save();
            }
            session()->flash('success', 'Se han activado todos los usuarios.');
        }
        return redirect()->route($this->route . 'index');
    }

    public function permissionsEdit($id)
    {
        $object = User::with(['permissions', 'roles.permissions'])->find($id);
        if (!$object) {
            session()->flash('warning', 'Usuario no encontrado.');
            return redirect()->route($this->route . 'index');
        }

        if ($object->id == 1) {
            session()->flash('warning', 'Este rol no puede ser editado.');
            return redirect()->route($this->route . 'index');
        }

        $permissions = Permission::orderBy('name')->where('guard_name', 'intranet')->get();
        $groups = $permissions->pluck('public_group')->unique();
        return view($this->folder . 'permissions', compact('object', 'permissions', 'groups'));
    }

    public function permissionsUpdate(Request $request, $id)
    {

        $object = User::find($id);

        if (!$object) {
            session()->flash('warning', 'Usuario no encontrado.');
            return redirect()->route($this->route . 'index');
        }
        if ($object->id == 1) {
            session()->flash('warning', 'Este usuario no puede ser modificado.');
            return redirect()->route($this->route . 'index');
        }
        $object->syncPermissions($request->permissions ?? []);
        $object->save();

        if ($object) {
            session()->flash('success', 'Permisos de usuario actualizado correctamente.');
            return redirect()->route($this->route . 'index');
        }
        $this->print();
        return redirect()->back()->withErrors(['mensaje' => 'Error inesperado al actualizar los permisos del usuario.'])->withInput();

    }

}
