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
                    <h1 class="font-30 bold text-center text-md-left" style="color: black;">Recuperación de contraseña</h1>
                </div>
                <div class="col-md-12">
                    <form action="{{ route('intranet.auth.send-password') }}" method="POST">
                        {{ csrf_field() }}
                        <div class="form-group has-feedback {{ $errors->has('email') ? 'has-error':'' }}">
                            <label for="email">Ingrese su correo para restablecer su contraseña</label>
                            <input type="text"
                                   class="form-control"
                                   placeholder="Email"
                                   name="email"
                                   id="email"
                                   value="{{ old('email') ? old('email') :'' }}">
                            <span class="glyphicon glyphicon-user form-control-feedback"></span>
                            {!! $errors->first('email','<span class="help-block">:message</span>') !!}
                        </div>
                        <div class="row">
                            <br/>
                            <div class="col-xs-12">
                                <button type="submit" class="btn btn-login btn-block" style="background-color: #f15a25; color: white">Enviar</button>
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
