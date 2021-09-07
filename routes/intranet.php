<?php

function getResourceRoutesForNameHelper($name)
{
    return [
        'index' => $name . ".index",
        'create' => $name . ".create",
        'store' => $name . ".store",
        'show' => $name . ".show",
        'edit' => $name . ".edit",
        'update' => $name . ".update",
        'destroy' => $name . ".destroy",
    ];
}

Route::namespace('Intranet')
//        ->domain('intranet.localhost')
    ->name('intranet.')
    ->prefix('intranet')
    ->group(function () {

        Route::get('/login', 'AuthController@show')->name('auth.show');
        Route::post('/login', 'AuthController@login')->name('auth.login');
        Route::get('/logout', 'AuthController@logout')->name('auth.logout');
        Route::post('/logout', 'AuthController@logout')->name('auth.logout');
        Route::get('/login/send-password', 'AuthController@showSendPassword')->name('auth.show-send-password');
        Route::post('/login/send-password', 'AuthController@sendPassword')->name('auth.send-password');
        Route::get('/login/recovery-password', 'AuthController@showRecoveryPassword')->name('auth.show-recovery-password');
        Route::post('/login/recovery-password', 'AuthController@recoveryPassword')->name('auth.recovery-password');

        Route::group(['middleware' => ['auth:intranet']], function () {

            Route::get('/', 'DashboardController@index')->name('dashboard');

            Route::post('users/active', 'UserController@active')->name('users.active');
//                Route::get('users/{user}/permissions', 'UserController@permissionsEdit')->name('users.permissionsEdit');
//                Route::put('users/{user}/permissions', 'UserController@permissionsUpdate')->name('users.permissionsUpdate');
            Route::post('users/change-status', 'UserController@changeStatus')->name('users.changeStatus');
//                Route::post('users/all-change', 'UserController@all_change')->name('users.all_change');
            Route::resource('users', 'UserController', ['names' => getResourceRoutesForNameHelper('users')]);
//
//                Route::post('roles/active', 'RoleController@active')->name('roles.active');
//                Route::post('roles/change-status', 'RoleController@changeStatus')->name('roles.changeStatus');
//                Route::resource('roles', 'RoleController', ['names' => getResourceRoutesForNameHelper('roles')]);
//

//            //EDITAR PERFIL
//            Route::get('profile', 'ProfileController@edit')->name('profile.edit');
//            Route::post('profile', 'ProfileController@update')->name('profile.update');
//
//            //WORKERS
//            Route::post('workers/active', 'WorkerController@active')->name('workers.active');
//            Route::resource('trabajadores', 'WorkerController', ['names' => getResourceRoutesForNameHelper('workers')]);
//
//            //ACCESS_CONTROL_WORKER_RECORDS
//            Route::post('access-control-worker-records/active', 'AccessControlWorkerRecordController@active')->name('accessControlWorkerRecords.active');
//            Route::resource('registro-entrada-trabajadores', 'AccessControlWorkerRecordController', ['names' => getResourceRoutesForNameHelper('accessControlWorkerRecords')]);
//
//            //ENTRY_REASON
//            Route::post('entry-reasons/active', 'EntryReasonController@active')->name('entryReasons.active');
//            Route::resource('motivos-ingreso', 'EntryReasonController', ['names' => getResourceRoutesForNameHelper('entryReasons')]);

        });
    });
