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
                        <div class="col-md-4">
                            <div class="row">
                                <div class="col-md-12">
                                    <div class="form-group" id="group-error-imagen">
                                        <label for="avatar">Imagen</label>
                                        <div class="image-product">
                                            @if(isset($object->image))
                                                <img id="image-product" src="{{ Storage::url($object->image) }}">
                                            @else
                                                <img id="image-product" src="/img/image-default.jpeg">
                                            @endif
                                        </div>
                                        <input type="file" name="image" id="file-image-product"
                                            class="inputfile" accept="image/x-png,image/gif,image/jpeg"/>
                                        <label for="file-image-product">Seleccione una Imagen</label>
                                        <span class="help-block" id="label-error-image"></span>
                                        <div class="link-del" onclick="deleteImg();"></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-8">
                            <div class="row">
                                <div class="col-md-12">
                                    <div class="form-group {{ $errors->has('title') ? 'has-error':'' }}">
                                        <label for="title">Título (*)</label>
                                        <input type="text"
                                            id="title" name="title"
                                            class="form-control"
                                            required
                                            value="{{ old('title') ?? $object->title }}">
                                        {!! $errors->first('title', '<span class="help-block">:message</span>') !!}
                                    </div>
                                </div>
                                <div class="col-md-12">
                                    <div class="form-group">
                                        <label for="content">Descripción (*)</label>
                                        <textarea name="description" id="content" rows="3" style="resize: none">{{ old('description') ?? $object->description }}</textarea>
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

    <script src="https://cdn.ckeditor.com/4.11.4/standard/ckeditor.js"></script>
    <script>
        var editor = CKEDITOR.replace('content', {
            language: 'es',
            entities_latin: false,
            enterMode : CKEDITOR.ENTER_BR,
            autoParagraph: false,
            resize_enabled: false,
            height: '280px',
            on: {
                change: function() {
                    checkContent(); 
                }
            }
        });
    </script>
    <script>
        $(document).ready(function() {
            if(CKEDITOR.instances['content'].getData()){
                contentcheck = true;
            } else {
                contentcheck = false;
            }
        });

        function checkContent(){
            if(CKEDITOR.instances['content'].getData()){
                contentcheck = true;
            } else {
                contentcheck = false;
            }
        }
    </script>
    <script>
        $("#form-create").submit(function(e){
            if(contentcheck == false){
                e.preventDefault();
                swal({
                    title: 'Debe llenar campo "Contenido"',
                    html: 'El campo contenido es obligatorio para finalizar el proceso',
                    type: 'error',
                    showCancelButton: false,
                    confirmButtonColor: '#43a047',
                    cancelButtonColor: '#d33',
                    confirmButtonText: 'Aceptar',
                    cancelButtonText: 'No, cancelar!'
                }).then(function (result) {
                    
                });
            } 
        });
    </script>

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