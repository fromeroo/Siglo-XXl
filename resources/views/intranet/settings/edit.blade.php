@extends('intranet.template.base')
@section('title', $config['blade']['viewTitle'])

@if ($config['blade']['showBreadcrumb'])
@section('breadcrumb')
    @foreach($config['breadcrumb'] as $key => $data)
        <li><a href="{{ $data['link'] }}"
               class="{{ count($config['breadcrumb']) == $key + 1 ? 'active' : '' }}">{{ $data['name'] }}</a></li>
    @endforeach
@endsection
@endif

@section('toolbar-buttons')
    <a href="{{route($config['route'] . 'index')}}" class="btn btn-default"><i
            class="fa fa-chevron-left"></i> {{ $config['blade']['btnBack']}}</a>
    <button class="btn btn-primary" type="button" onclick="doSubmit('form-edit')"><i
            class="fa fa-save"></i> {{ $config['blade']['btnUpdate']}}</button>
@endsection

@section('content')
    <form id="form-edit" action="{{ route($config['route'] . 'update', ['object' => $object->id]) }}" enctype="multipart/form-data" method="POST">

        <button type="submit" class="hide"></button>
        <input type="hidden" name="_method" value="PUT">
        @csrf()

        <div class="row">
            <div class="col-md-10 col-md-offset-1">
                <div class="panel">
                    <div class="panel-body">
                        <div class="col-md-12">
                            <div class="row">
                                <div class="col-md-6">
                                    <div class="form-group {{ $errors->has('user') ? 'has-error':'' }}">
                                        <label for="user">Usuario (*)</label>
                                        <input type="text"
                                            id="user" name="user"
                                            class="form-control"
                                            required
                                            value="{{ old('user') ?? $object->user }}">
                                        {!! $errors->first('user', '<span class="help-block">:message</span>') !!}
                                    </div>
                                </div>
                                <div class="col-md-6">
                                    <div class="form-group {{ $errors->has('password') ? 'has-error':'' }}">
                                        <label for="password">Contraseña (*)</label>
                                        <input type="password"
                                            id="password" name="password"
                                            class="form-control"
                                            required
                                            value="{{ old('password') }}">
                                        {!! $errors->first('password', '<span class="help-block">:message</span>') !!}
                                    </div>
                                </div>
                              
                                
                                <div class="col-md-6">
                                    <div class="form-group {{ $errors->has('hotel_id') ? 'has-error':'' }}">
                                        <label for="hotel_id">Hotel (*)</label>
                                        <select id="hotel_id" name="hotel_id" class="form-control">
                                            @if($hotelFound)
                                                <option value="{{$hotelFound->id}}" selected>{{$hotelFound->name}}</option>
                                            @else
                                                <option value="" selected disabled>Seleccione una opción</option>
                                            @endif
                                            @if($hotels)
                                                @foreach($hotels as $key => $hotel)
                                                    <option value="{!! $hotel->id !!}">{!! $hotel->name !!}</option>
                                                @endforeach
                                            @endif
                                        </select>
                                        {!! $errors->first('title', '<span class="help-block">:message</span>') !!}
                                    </div>
                                </div>
                                <div class="col-md-6">
                                    <div class="form-group {{ $errors->has('distance_unit_id') ? 'has-error':'' }}">
                                        <label for="distance_unit_id">Unidad de distancia (*)</label>
                                        <select id="distance_unit_id" name="distance_unit_id" class="form-control">
                                            @if($distanceUnitFound)
                                                <option value="{{$distanceUnitFound->id}}" selected>{{$distanceUnitFound->name}}</option>
                                            @else
                                                <option value="" selected disabled>Seleccione una opción</option>
                                            @endif
                                            @if($distanceUnits)
                                                @foreach($distanceUnits as $key => $distanceUnit)
                                                    <option value="{!! $distanceUnit->id !!}">{!! $distanceUnit->name !!}</option>
                                                @endforeach
                                            @endif
                                        </select>
                                        {!! $errors->first('title', '<span class="help-block">:message</span>') !!}
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-md-12" style="font-style: italic;">
                                Los campos con (*) son obligatorios.
                            </div>
                        </div>

                        <div class="panel-footer">
                            <div class="row">
                                <div class="col-xs-6">
                                    <a href="{{route($config['route'] . 'index')}}" class="btn btn-default">
                                        <i class="fa fa-chevron-left"></i> {{ $config['blade']['btnBack']}}
                                    </a>
                                </div>
                                <div class="col-xs-6 text-right">
                                    <button class="btn btn-primary" type="submit">
                                        <i class="fa fa-save"></i> {{ $config['blade']['btnUpdate']}}
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </form>
@endsection

@section('styles')
    <!--Bootstrap Select [ OPTIONAL ]-->
    <link href="/themes/intranet/plugins/select2/css/select2.min.css" rel="stylesheet">
    <style>
        .image-product {
            width: 100%;
            height: 235px;
            border: 1px solid #c5c5c5;
            padding: 5px;
            margin-bottom: 10px;
            display: flex;
            background: #f5f5f5;
        }

        a.cke_dialog_ui_button_ok {
            color: #fff;
            background-color: #000000;
            border-color: rgb(25, 118, 210);
        }

        .image-product img {
            width: 100%;
            object-fit: cover;
        }

        .image-product:after {
            content: "";
            display: block;
            padding-bottom: 100%;
        }

        .inputfile {
            width: 0.1px;
            height: 0.1px;
            opacity: 0;
            overflow: hidden;
            position: absolute;
            z-index: -1;
        }

        .inputfile + label {
            font-size: 1.25em;
            font-weight: 700;
            color: white !important;
            width: 100%;
            background-color: #000000;
            border-color: #126002;
            display: inline-block;
            padding: 6px 12px;
            margin-bottom: 0;
            font-size: 14px;
            font-weight: 400;
            line-height: 1.42857143;
            text-align: center;
            white-space: nowrap;
            vertical-align: middle;
            -ms-touch-action: manipulation;
            touch-action: manipulation;
            cursor: pointer;
            -webkit-user-select: none;
            -moz-user-select: none;
            -ms-user-select: none;
            user-select: none;
            background-image: none;
            border: 1px solid transparent;
        }

        .inputfile:focus + label,
        .inputfile + label:hover {
            background-color: #000000;
            border-color: #000000;
        }

        .link-del {
            text-align: center;
            color: #000000;
            margin-top: 5px;
            cursor: pointer;
        }
    </style>
@endsection

@section('scripts')
    <!--Bootstrap Select [ OPTIONAL ]-->
    <script src="/themes/intranet/plugins/select2/js/select2.min.js"></script>

    <script>
        $(".select2").select2({
            tags: true
        });

        /* password generator */
        function generatePassword() {
            var pass = Math.random().toString(36).substring(2);
            $('#password').val(pass);
        }
    </script>

    <script src="/themes/intranet/plugins/rut/jquery.rut.js"></script>

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

            $('.image-product').css('height', $('.image-product').innerWidth())
        });
    </script>

    <script>
        function readURL(input) {
            if (input.files && input.files[0]) {
                var reader = new FileReader();
                reader.onload = function (e) {
                    $('#image-product').attr('src', e.target.result);
                    $('.link-del').html($('<i class="fa fa-trash"></i> <span>Eliminar</span>'));
                };
                reader.readAsDataURL(input.files[0]);
            }
        }

        $("#file-image-product").change(function () {
            readURL(this);
        });

        function deleteImg() {
            $('#image-product').attr('src', '/img/image-default.jpeg');
            $('.link-del').html('');
            $("#file-image-product").val('');
        }

    </script>

    <script>
        function checkKey(name) {
            var clean = $('#' + name).val().replace(/[^0-9Kk]/g, "");
            // don't move cursor to end if no change
            if (clean !== $('#' + name).val()) $('#' + name).val(clean);
        }
    </script>
@endsection