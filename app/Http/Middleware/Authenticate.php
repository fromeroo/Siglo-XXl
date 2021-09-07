<?php

namespace App\Http\Middleware;

use Illuminate\Auth\Middleware\Authenticate as Middleware;

class Authenticate extends Middleware
{
    /**
     * Get the path the user should be redirected to when they are not authenticated.
     *
     * @param \Illuminate\Http\Request $request
     * @return string
     */

    protected $guards = [];

    // public function handle($request, Closure $next, ...$guards)
    // {
    //     $this->guards = $guards;
    //     return parent::handle($request, $next, ...$guards);
    // }

    protected function redirectTo($request)
    {
        // if (!$request->expectsJson()) {
        //     if (in_array('intranet', $this->guards)) {
        //         return route('intranet.auth.show');
        //     }
        //     return route('customer.auth.show');
        // }
        return redirect()->intended(route('intranet.dashboard'));
    }
}
