<!DOCTYPE html>
<html class="wide wow-animation" lang="es">

<head>
  <title>Inland | @yield('page-title')</title>
  <meta name="viewport" content="width=device-width height=device-height initial-scale=1.0">
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <!--<link rel="icon" href="images/favicon.ico" type="image/x-icon">-->
  <link rel="stylesheet" type="text/css" href="//fonts.googleapis.com/css?family=Open+Sans:300,400,600,700,800%7CMuli:100,300,400,600,800">
  <link rel="stylesheet" href="{{asset('css/bootstrap.css')}}">
  <link rel="stylesheet" href="{{asset('css/fonts.css')}}">
  <link rel="stylesheet" href="{{asset('css/style.css')}}">
  <link rel="stylesheet" href="{{asset('css/novi.css')}}">
  <link rel="stylesheet" href="{{asset('themes/intranet/plugins/sweet-alert/sweetalert2.min.css')}}">

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

  <style>
    .ie-panel {       display: none;       background: #212121;       padding: 10px 0;       box-shadow: 3px 3px 5px 0 rgba(0, 0, 0, .3);       clear: both;       text-align: center;       position: relative;       z-index: 1;     }      html.ie-10 .ie-panel,     html.lt-ie-10 .ie-panel {       display: block;     }
  </style>
  @yield('styles')
</head>

<body>
  <div class="ie-panel">
    <a href="http://windows.microsoft.com/en-US/internet-explorer/"><img src="images/ie8-panel/warning_bar_0000_us.jpg" height="42" width="820" alt="You are using an outdated browser. For a faster, safer browsing experience, upgrade for free today."></a>
  </div>
  <div class="preloader" id="loading">
    <div class="preloader-body">
      <div id="loading-center-object">
        <div class="object" id="object_four"></div>
        <div class="object" id="object_three"></div>
        <div class="object" id="object_two"></div>
        <div class="object" id="object_one"></div>
      </div>
    </div>
  </div>
  <div class="page">
    @yield('content')
  </div>
  <div class="snackbars" id="form-output-global"></div>
  <script src="{{asset('js/core.min.js')}}"></script>
  <script src="{{asset('js/script.js')}}"></script>
  <script src="{{asset('themes/intranet/plugins/sweet-alert/sweetalert2.all.js')}}"></script>
  <script src="{{asset('themes/intranet/plugins/sweet-alert/sweetalert2.min.js')}}"></script>
   @yield('scripts')
</body>

</html>