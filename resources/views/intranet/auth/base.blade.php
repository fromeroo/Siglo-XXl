<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">

    <title>{{  env('INTRANET_NAME', 'Intranet') }} | @yield('title', 'Login')</title>

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
    @include('intranet.template.components.theme')

    <link href="/themes/intranet/css/custom.css" rel="stylesheet">

    <link rel="apple-touch-icon" sizes="180x180" href="/themes/intranet/img/logos/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="/themes/intranet/img/logos/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/themes/intranet/img/logos/favicon-16x16.png">
    <link rel="manifest" href="/themes/intranet/img/logos/site.webmanifest">
    <link rel="mask-icon" href="/themes/intranet/img/logos/safari-pinned-tab.svg" color="#c5192b">
    <meta name="apple-mobile-web-app-title" content="INLAND">
    <meta name="application-name" content="INLAND">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="theme-color" content="#ffffff">

    <style>
        .btn:not(.disabled):not(:disabled):hover {
             box-shadow: none;
        }

        body{
            background-attachment:fixed;
            background-repeat: no-repeat;
            background-size: cover;
        }
    </style>

    @yield('styles')

</head>

<body style="background: white;">

@include('intranet.template.components.loading')

<div id="container" class="bg-white">
    @yield('content')
</div>
<!--===================================================-->
<!-- END OF CONTAINER -->


<!--JAVASCRIPT-->
<!--=================================================-->

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

<script src="/themes/intranet/js/custom.js"></script>

<script src="/themes/intranet/plugins/rut/jquery.rut.js"></script>

@yield('scripts')

<!--Bootstrap toggle [ OPTIONAL ] ALLWAYS BEFORE BS TABLE -->
<script src="/themes/intranet/plugins/bootstrap-toggle/bootstrap-toggle.min.js"></script>

<script src="/themes/intranet/js/globals.js"></script>

</body>
</html>
