<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="csrf-token" content="{{ csrf_token() }}">
    <title>{{  env('INTRANET_NAME', 'Intranet') }} | @yield('title', 'Dashboard')</title>

    <!--Open Sans Font [ OPTIONAL ]-->
    <link href='https://fonts.googleapis.com/css?family=Open+Sans:400,300,600,700' rel='stylesheet' type='text/css'>

    <!--Bootstrap Stylesheet [ REQUIRED ]-->
    <link href="/themes/intranet/css/bootstrap.min.css" rel="stylesheet">

    <!--Font Awesome [ OPTIONAL ]-->
    <link href="/themes/intranet/plugins/font-awesome/css/font-awesome.min.css" rel="stylesheet">

    <!--Themify Icons [ OPTIONAL ]-->
    <link href="/themes/intranet/plugins/themify-icons/themify-icons.min.css" rel="stylesheet">

    <!--Nifty Stylesheet [ REQUIRED ]-->
    <link href="/themes/intranet/css/nifty.min.css" rel="stylesheet">

    <!--SweetAlert [ OPTIONAL ]-->
    <link href="/themes/intranet/plugins/sweet-alert/sweetalert2.min.css" rel="stylesheet">

    <!--Toast [ OPTIONAL ]-->
    <link href="/themes/intranet/plugins/toastr/toastr.min.css" rel="stylesheet">

    <!--Toast [ OPTIONAL ]-->
    <link href="/themes/intranet/plugins/select2/css/select2.min.css" rel="stylesheet">

    <!--Bootstrap toggle [ OPTIONAL ]-->
    <link href="/themes/intranet/plugins/bootstrap-toggle/bootstrap-toggle.min.css" rel="stylesheet">

    <!--Nifty Premium Icon [ DEMONSTRATION ]-->
    <link href="/themes/intranet/css/demo/nifty-demo-icons.min.css" rel="stylesheet">

    <link href="/themes/intranet/plugins/summernote/summernote.min.css" rel="stylesheet">

    <link rel="apple-touch-icon" sizes="180x180" href="/themes/intranet/img/logos/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="/themes/intranet/img/logos/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/themes/intranet/img/logos/favicon-16x16.png">
    <link rel="manifest" href="/themes/intranet/img/logos/site.webmanifest">
    <link rel="mask-icon" href="/themes/intranet/img/logos/safari-pinned-tab.svg" color="#5bbad5">
    <meta name="apple-mobile-web-app-title" content="INLAND Intranet">
    <meta name="application-name" content="INLAND Intranet">
    <meta name="msapplication-TileColor" content="#848484">
    <meta name="theme-color" content="#ffffff">

    <meta name="title" content="Inland">
    <meta name="description"
          content="Amazing Geo Guide">
    <meta name="keywords"
          content="inland, geologia, guia, turismo, tierra, viajes, planes">
    <meta name="robots" content="index, nofollow">
    <meta name="language" content="Spanish">
    <meta name="revisit-after" content="4000 days">
    <meta name="author" content="Inland">
    <meta name="rights" content="Inland"/>

    <meta property="og:site_name" content="Inland">
    <meta property="og:title" content="Inland"/>
    <meta property="og:description"
          content="Amazing Geo Guide"/>
    <meta property="og:image" itemprop="image" content="https://inland.cl/images/logo-1.png">
    <meta property="og:type" content="website"/>
    <meta property="og:updated_time" content="1440432930"/>
    <meta property="og:url" content="https://www.inland.cl/"/>

    <!--=================================================-->


    <!--Pace - Page Load Progress Par [OPTIONAL]-->
    {{--<link href="/themes/intranet/plugins/pace/pace.min.css" rel="stylesheet">--}}
    {{--<script src="/themes/intranet/plugins/pace/pace.min.js"></script>--}}


    <!--Demo [ DEMONSTRATION ]-->
    @include('intranet.template.components.theme')

    <link href="/themes/intranet/plugins/bootstrap-table/bootstrap-table.min.css" rel="stylesheet">
    <link href="/themes/intranet/css/custom.css" rel="stylesheet">
    <link rel="stylesheet" href="/themes/intranet/plugins/air_datepicker/datepicker.min.css">

    @yield('styles')

    <style>
        @media (max-width: 500px) {
            .logo-img {
                width: 40%;
            }
        }

        .swal-wide {
            width: 700px !important;
            height: 450px !important;
        }

        .swal2-popup {
            font-size: 1.6rem !important;
        }

        .swal2-icon.swal2-info, .swal2-icon.swal2-question, .swal2-icon.swal2-warning, .swal2-icon.swal2-success {
            font-size: 3.35em !important;
        }

        .swal2-popup .swal2-title {
            margin-top: 20px !important;
        }

        .swal2-popup .swal2-actions {
            margin-top: 40px !important;
        }

        .datepicker--cell.-selected-, .datepicker--cell.-selected-.-current-, .datepicker--cell.-selected-focus-, .datepicker--cell.-focus-, .datepicker--cell.-current-focus- {
            color: #fff !important;
            background: #C41F2F !important;
        }

        .datepicker--cell.-current- {
            color: #C41F2F !important;
        }

        .datepicker--button {
            color: #C41F2F !important;
        }

        .note-statusbar{
            display: none;
        }

        .toggle-group .btn-success{
            background-color: #f15a25 !important;
            border-color: #f15a25 !important;
        }

        .swal2-styled.swal2-confirm {
            border: 0;
            border-radius: .25em;
            background-color: #f15a25 !important;
            color: #fff;
            font-size: 1.0625em;
        }

        @media (min-width: 768px){
            #container.mainnav-sm .brand-icon {
                content: url("/img/logo_mini.png");
                margin-top: 10px !important;
                padding-left: 0px !important;
                margin-left: 18px !important;
                width: 20px !important;
            }
        }

        @import url(https://fonts.googleapis.com/css?family=Give+You+Glory|The+Girl+Next+Door|Gloria+Hallelujah|Indie+Flower);

        body {
        background: #eee;
        }
        .sticky {
        -webkit-box-shadow: #DDD 0px 1px 2px;
        position: relative;
        background-color: #F4F39E;
        border-color: #DEE184;
        color: #47576B;
        text-align: center;
        margin: 2.5em 0px;
        padding: 1.5em 1em;
        -webkit-box-shadow: 0px 1px 3px rgba(0,0,0,0.25);
        -moz-box-shadow: 0px 1px 3px rgba(0,0,0,0.25);
        box-shadow: 0px 1px 3px rgba(0,0,0,0.25);
        width: 250px;
        font-family: 'Indie Flower', cursive;
        font-family: 'Give You Glory', cursive;
        font-family: 'The Girl Next Door', cursive;
        font-family: 'Gloria Hallelujah', cursive;
        }
        .post-it {
        display: table;
        margin: 5em auto 0;  
        }
        .taped {
        display: table-cell;
        text-align: center;
        vertical-align: middle;
        }
        .sticky.taped:after {
        display: block;
        content: "";
        position: absolute; 
        width: 110px;
        height: 30px;
        top: -21px;
        left: 30%;    
        border: 1px solid #fff;
        background: rgba(254, 254, 254, .6);
        -webkit-box-shadow: 0px 0 3px rgba(0,0,0,0.1);
        -moz-box-shadow: 0px 0 3px rgba(0,0,0,0.1);
        box-shadow: 0px 0 3px rgba(0,0,0,0.1);  
        }

        .note { 
        -webkit-box-shadow: #DDD 0px 1px 2px;
        position: relative;
        background-color: #F4F39E;
        border-color: #DEE184;
        text-align: center;
        margin: 1.5em auto;
        padding: 1.5em 1em;
        -webkit-box-shadow: 0px 1px 3px rgba(0,0,0,0.25);
        -moz-box-shadow: 0px 1px 3px rgba(0,0,0,0.25);
        box-shadow: 0px 1px 3px rgba(0,0,0,0.25);
        -webkit-transform: rotate(2deg);
        -moz-transform: rotate(2deg);
        -o-transform: rotate(2deg);
        -ms-transform: rotate(2deg);
        transform: rotate(2deg);
        width: 250px;
        font-family: 'The Girl Next Door', cursive; /*originally with brain flower font*/
        font-size: 1em;
        }
        .note:after {
        display: block;
        content: "";
        position: absolute; 
        width: 110px;
        height: 30px;
        top: -21px;
        left: 30%;    
        border: 1px solid #fff;
        background: rgba(254, 254, 254, .6);
        -webkit-box-shadow: 0px 0 3px rgba(0,0,0,0.1);
        -moz-box-shadow: 0px 0 3px rgba(0,0,0,0.1);
        box-shadow: 0px 0 3px rgba(0,0,0,0.1);  
        }

    </style>

</head>

<!--TIPS-->
<!--You may remove all ID or Class names which contain "demo-", they are only used for demonstration. -->
<body>

@include('intranet.template.components.loading')

<div id="container" class="effect aside-bright mainnav-lg footer-fixed navbar-fixed aside-fixed mainnav-fixed">

    <!--NAVBAR-->
    <!--===================================================-->
@include('intranet.template.layouts.navbar')
<!--===================================================-->
    <!--END NAVBAR-->

    <div class="boxed">

        <!--CONTENT CONTAINER-->
        <!--===================================================-->
        <div id="content-container">
            <div id="page-head">
                <div class="row">

                    <div class="col-sm-7">
                        <!--Page Title-->
                        <!--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-->
                        <div id="page-title">
                            <h1 class="page-header text-overflow">@yield('title', 'Titulo')</h1>
                        </div>
                        <!--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-->
                        <!--End page title-->


                        <!--Breadcrumb-->
                        <!--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-->
                        <ol class="breadcrumb">
                            <li><a href="{{ route('intranet.dashboard') }}"><i class="demo-pli-home"></i></a></li>
                            @yield('breadcrumb')
                        </ol>
                    </div>
                    <div class="col-sm-5 text-right" style="padding-right: 30px;padding-top: 45px;">
                        @yield('toolbar-buttons')
                    </div>
                </div>


                <!--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-->
                <!--End breadcrumb-->

            </div>
        {{--<div id="page-head">--}}
        {{--<div class="pad-all text-center">--}}
        {{--<h3>Welcome back to the Dashboard.</h3>--}}
        {{--<p>Scroll down to see quick links and overviews of your Server, To do list, Order status or get some Help using Nifty.</p>--}}
        {{--</div>--}}
        {{--</div>--}}


        <!--Page content-->
            <!--===================================================-->
            <div id="page-content">
                @include('intranet.template.components._alerts')

                @yield('content')

            </div>
            <!--===================================================-->
            <!--End page content-->

        </div>
        <!--===================================================-->
        <!--END CONTENT CONTAINER-->


        <!--ASIDE-->
        <!--===================================================-->

    @include('intranet.template.layouts.aside-container')
    <!--===================================================-->
        <!--END ASIDE-->


        <!--MAIN NAVIGATION-->
        <!--===================================================-->
    @include('intranet.template.layouts.main-nav')
    <!--===================================================-->
        <!--END MAIN NAVIGATION-->

    </div>


    <!-- FOOTER -->
    <!--===================================================-->
@include('intranet.template.layouts.footer')
<!--===================================================-->
    <!-- END FOOTER -->


    <!-- SCROLL PAGE BUTTON -->
    <!--===================================================-->
    <button class="scroll-top btn">
        <i class="pci-chevron chevron-up"></i>
    </button>
    <!--===================================================-->
</div>
<script src="/js/app.js"></script>
<!--===================================================-->
<!-- END OF CONTAINER -->


<!--JAVASCRIPT-->
<!--=================================================-->
<script src="https://polyfill.io/v3/polyfill.min.js?features=default"></script>
<!--jQuery [ REQUIRED ]-->
<script src="/themes/intranet/js/jquery.min.js"></script>

<!--BootstrapJS [ RECOMMENDED ]-->
<script src="/themes/intranet/js/bootstrap.min.js"></script>

<!--NiftyJS [ RECOMMENDED ]-->
<script src="/themes/intranet/js/nifty.min.js"></script>

<!--Bootbox Modals [ OPTIONAL ]-->
<script src="/themes/intranet/plugins/bootbox/bootbox.min.js"></script>

<!--SweetAlert [ OPTIONAL ]-->
<script src="/themes/intranet/plugins/sweet-alert/sweetalert2.min.js"></script>

<!--Toast [ OPTIONAL ]-->
<script src="/themes/intranet/plugins/toastr/toastr.min.js"></script>

<!--Select 2 [ OPTIONAL ]-->
<script src="/themes/intranet/plugins/select2/js/select2.min.js"></script>


<script src="/themes/intranet/js/globals.js"></script>

<!--Bootstrap table [ OPTIONAL ]-->
<script src="/themes/intranet/plugins/bootstrap-table/bootstrap-table.min.js"></script>


<script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-table/1.12.1/locale/bootstrap-table-es-CL.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-table/1.12.1/extensions/cookie/bootstrap-table-cookie.min.js"></script>

<script src="/themes/intranet/plugins/bootstrap-table/extensions/export/bootstrap-table-export.js"></script>
<script src="/themes/intranet/js/custom.js"></script>
<script src="/themes/intranet/plugins/summernote/summernote.min.js"></script>

<!--Bootstrap toggle [ OPTIONAL ] ALLWAYS BEFORE BS TABLE -->
<script src="/themes/intranet/plugins/bootstrap-toggle/bootstrap-toggle.min.js"></script>


<script>
    $(document).ready(function () {
        $('.loader').fadeOut();
        $('body').removeClass('overflow-hidden');
    });

    $(window).on('beforeunload', function () {
        $('body').addClass('overflow-hidden');
        $('.loader').fadeIn();
    });

    $(document).ready(function() {
        $('.summernote').summernote({
            disableResizeEditor: true,
            callbacks: {
                onFocus: function (contents) {
                    if($('.summernote').summernote('isEmpty')){
                        $(".summernote").html(''); 
                    }
                }
            }
        });
    });
</script>

<script>
    $(document).ready(function () {
        $('.select2').select2({
            language: {
                noResults: function (params) {
                    return "No se han encontrado resultados.";
                }
            }
        });
    });

    function validarAccion() {
        var form = $('#form_massive_email');

        swal({
            title: '¿Estas Seguro?',
            text: "Esta acción enviará un email a todos los clientes y abrirá la posibilidad de que puedan editar sus formularios",
            type: 'warning',
            customClass: 'swal-wide',
            showCancelButton: true,
            confirmButtonColor: '#43a047',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Si, ¡estoy seguro!',
            cancelButtonText: 'No, ¡cancelar!'
        }).then(function (result) {
            if (result.value) {
                form.submit();
            }
        })

    }
</script>

<script>
    try {

        jQuery.fn.bootstrapTable.defaults.icons = {
            paginationSwitchDown: 'demo-pli-arrow-down',
            paginationSwitchUp: 'demo-pli-arrow-up',
            refresh: 'demo-pli-repeat-2',
            toggle: 'demo-pli-layout-grid',
            columns: 'demo-pli-check',
            detailOpen: 'demo-psi-add',
            detailClose: 'demo-psi-remove'
        };
    } catch (error) {

    }
</script>

@yield('scripts')

</body>
</html>
