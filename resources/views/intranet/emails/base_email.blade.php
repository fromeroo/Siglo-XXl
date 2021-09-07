<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Boletín</title>
    <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700&display=swap" rel="stylesheet">
    <link id="theme" href="/themes/intranet/css/themes/type-a/theme-ocean.min.css" rel="stylesheet">

    <meta name="viewport" content="width=divece-whitd,initial-scale=1">
    <style>
        .contenedor {
            font-family: 'Montserrat', sans-serif;
            max-width: 600px;
            margin: 30px auto;
            padding: 0px;
            -webkit-box-shadow: 0px 0px 5px 0px rgba(0, 0, 0, 0.21);
            -moz-box-shadow: 0px 0px 5px 0px rgba(0, 0, 0, 0.21);
            box-shadow: 0px 0px 5px 0px rgba(0, 0, 0, 0.21);
            border-radius: 10px;
            border: solid 1px #ccc !important;
            color: #eee !important;
        }

        .cabecera {
            width: 100%;
            padding-bottom: 20px;
            text-align: center;
            padding-top: 20px;
        }

        .pie {
            background: #eee;
            margin-top: 20px;
            text-align: center;
            padding: 30px 0px;
        }

        .masinfo {
            font-size: 14px;
            padding-bottom: 10px;
            color: #757575;
        }

        .web a {
            font-size: 20px;
            color: #757575;
            text-decoration: none;
            font-weight: 700;
        }

        .disenado {
            padding-top: 20px;
            font-size: 12px;
            color: #999;
            text-decoration: none;
        }

        .disenado a {
            padding-top: 20px;
            font-size: 12px;
            color: #999;
            text-decoration: none;
        }

        .cabecera img {
            max-width: 170px;
            
        }

        .text-legal {
            text-align: left;
            padding-top: 30px;
            font-size: 12px;
            color: #999;
        }

        .titulo {
            font-size: 20px !important;
            font-weight: 700 !important;
            color: #001B36 !important;
            padding-bottom: 10px !important;
        }

        .cuerpo-email {
            text-align: left;
            max-width: 90%;
            margin: 20px auto;
            font-size: 14px;
        }

        .mensaje {
            color: #000 !important;
        }

        .table {
            width: 100%;
            /*border-collapse: separate;*/
            /*border-spacing: 2px;*/
        }

        table {
            border-collapse: collapse;
        }

        table, th, td {
            border: 1px solid #e8e8e8;
            padding: 5px 10px;
            /*border-spacing: 2px;*/
        }

        table th {
            background-color: #f15a25;
            color: #ffffff;
            padding: 5px;
        }

        .bold {
            font-weight: bold;
        }

        .w-25 {
            width: 20%;
        }

        .img-logo{
            background-color: #f15a25;
            border-radius: 30px;
            padding-right: 20px !important;
        }
    </style>
</head>
<body>

<div class="contenedor">
    <div class="cabecera">
        <img class="img-logo" src="https://thecoolbridge.com/images/logo-tcb.png"/>
    </div>
    <div class="cuerpo-email">

        @yield('content')

    </div>
    <div class="pie">
        <div class="masinfo">Ingresa a la pagina web:</div>
        <div class="web"><a href="https://inland.cl/" target="_blank">www.inland.cl</a></div>
    </div>
</div>

<br/>

</body>
</html>
