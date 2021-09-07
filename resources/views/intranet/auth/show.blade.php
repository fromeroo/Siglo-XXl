@extends('intranet.auth.base')

@section('content')

    <div class="row bg-white" style="height: 100%; overflow-y:auto">
        <div class="col-md-6 d-flex h-100">
            <div class="row m-none m-md-auto  px-3 px-md-5 " style="max-width: 500px;">
                <div class="col-md-12 py-4 text-center" style="margin-top:100px">
                    <img src="/img/logo.png" alt="">
                </div>
                <div class="col-md-12">
                    @include('intranet.template.components._success')
                    @include('intranet.template.components._danger')
                </div>
                <div class="col-md-12 py-4">
                    <h1 class="font-30 bold text-center text-md-left" style="color: black;">¡Bienvenido/a de vuelta!</h1>
                </div>
                <div class="col-md-12">
                    <form action="{{ route('intranet.auth.login') }}" method="POST">
                        {{ csrf_field() }}
                        <div class="form-group has-feedback {{ $errors->has('email') ? 'has-error':'' }}">
                            <label for="email">Correo electrónico:</label>
                            <input type="email"
                                   class="form-control"
                                   placeholder="Email"
                                   id="email"
                                   name="email"
                                   value="{{ old('email') }}">
                            <span class="glyphicon glyphicon-envelope form-control-feedback"></span>
                            {!! $errors->first('email','<span class="help-block">:message</span>') !!}

                        </div>
                        <div class="form-group has-feedback {{ $errors->has('password') ? 'has-error':'' }}">
                            <label for="password">Contraseña:</label>
                            <input type="password"
                                    class="form-control"
                                    placeholder="Contraseña"
                                    name="password">
                            <span class="glyphicon glyphicon-lock form-control-feedback"></span>
                            {!! $errors->first('password','<span class="help-block">:message</span>') !!}
                        </div>
                        <div class="row">
                            <div class="col-xs-12 form-group has-feedback {{ $errors->has('error') ? 'has-error':'' }}">
                                <input type="hidden" name="error">
                                {!! $errors->first('error','<span class="help-block">:message</span>') !!}
                            </div>

                            <div class="col-xs-12">
                                <button type="submit" class="btn btn-login btn-block" style="background-color: #f15a25; color: white">Iniciar sesión</button>
                            </div>

                            <div class="col-xs-12 py-5 px-3 d-flex">
                                <div class="mx-auto d-flex" style="border-bottom: 1px solid #7a878e; width: 90%;">
                                        <div class="mx-auto" style="width: 40px; padding-left: 15px; margin-bottom: -7px; background: white;">o</div>
                                </div>
                            </div>
                            <div class="col-xs-12">
                            <button type="button" onclick="location.href='{{ route('intranet.auth.show-send-password') }}'" class="btn btn-login btn-block" style="background-color: #f15a25; color: white">Recuperar contraseña</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
        <div class="col-md-6 d-none d-md-block">
            <img src="/img/fondo.jpg" style="width:100%; height: 100vh; object-fit: cover;"/>
        </div>
    </div>

@endsection
@section('styles')
    <style>
        .form-control,
        .btn-login{
            height: 50px;
        }
        .has-feedback label~.form-control-feedback {
            top: 31px;
        }
    </style>
@endsection
@section('scripts')
    <script>
        $(function () {
            $("input#rut").rut({
                formatOn: 'keyup',
                validateOn: 'change' // si no se quiere validar, pasar null
            }).on('rutInvalido', function () {
                showToastError("El rut " + $(this).val() + " es inválido");
                $(this).parents(".form-group").addClass("has-error");
                $(this).val("");
            }).on('rutValido', function () {
                $(this).parents(".form-group").removeClass("has-error")
            });

        });
    </script>

    <script>
        function checkKey(name) {
            var clean = $('#' + name).val().replace(/[^0-9Kk]/g, "");
            // don't move cursor to end if no change
            if (clean !== $('#' + name).val()) $('#' + name).val(clean);
        }
    </script>
@endsection
