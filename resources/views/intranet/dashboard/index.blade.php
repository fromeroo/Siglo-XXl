@extends('intranet.template.base')
@section('title', 'Dashboard')
@section('breadcrumb')
<li>Página Principal</li>
@endsection

@section('content')
@can('intranet.dashboard')
    
<div class="row">
    
    <div class="col-sm-6 col-lg-3">
        <div class="panel media pad-all">
            <div class="media-left">
                <span class="icon-wrap icon-wrap-sm icon-circle bg-success">
                    <i class="ti-notepad fa-2x"></i>
                </span>
            </div>
            
            <div class="media-body">
                <p class="text-2x mar-no text-thin">{{$guideCount}}</p>
                <p class="text-muted mar-no">Guías</p>
            </div>
        </div>
    </div>
    <div class="col-sm-6 col-lg-3">
        <div class="panel media pad-all">
            <div class="media-left">
                <span class="icon-wrap icon-wrap-sm icon-circle bg-info">
                    <i class="ti-map-alt fa-2x"></i>
                </span>
            </div>
            
            <div class="media-body">
                <p class="text-2x mar-no text-thin">{{$regionCount}}</p>
                <p class="text-muted mar-no">Regiones</p>
            </div>
        </div>
    </div>
    <div class="col-sm-6 col-lg-3">
        <div class="panel media pad-all">
            <div class="media-left">
                <span class="icon-wrap icon-wrap-sm icon-circle bg-warning">
                    <i class="ti-direction fa-2x"></i>
                </span>
            </div>
            
            <div class="media-body">
                <p class="text-2x mar-no text-thin">{{$placeCount}}</p>
                <p class="text-muted mar-no">Lugares</p>
            </div>
        </div>
    </div>
    <div class="col-sm-6 col-lg-3">
        <div class="panel media pad-all">
            <div class="media-left">
                <span class="icon-wrap icon-wrap-sm icon-circle bg-danger">
                    <i class="ti-image fa-2x"></i>
                </span>
            </div>
            
            <div class="media-body">
                <p class="text-2x mar-no text-thin">{{$trekkingCount}}</p>
                <p class="text-muted mar-no">Trekkings</p>
            </div>
        </div>
    </div>
    <div class="col-sm-6 col-lg-3">
        <div class="panel media pad-all">
            <div class="media-left">
                <span class="icon-wrap icon-wrap-sm icon-circle bg-success">
                    <i class="ti-face-smile fa-2x"></i>
                </span>
            </div>
            
            <div class="media-body">
                <p class="text-2x mar-no text-thin">{{$clientCount}}</p>
                <p class="text-muted mar-no">Clientes</p>
            </div>
        </div>
    </div>
    <div class="col-sm-6 col-lg-3">
        <div class="panel media pad-all">
            <div class="media-left">
                <span class="icon-wrap icon-wrap-sm icon-circle  bg-info">
                    <i class="ti-package fa-2x"></i>
                </span>
            </div>
            
            <div class="media-body">
                <p class="text-2x mar-no text-thin">{{$equipmentItemCount}}</p>
                <p class="text-muted mar-no">Equipamientos</p>
            </div>
        </div>
    </div>
    <div class="col-sm-6 col-lg-3">
        <div class="panel media pad-all">
            <div class="media-left">
                <span class="icon-wrap icon-wrap-sm icon-circle bg-warning">
                    <i class="ti-comments fa-2x"></i>
                </span>
            </div>
            
            <div class="media-body">
                <p class="text-2x mar-no text-thin">{{$commentCount}}</p>
                <p class="text-muted mar-no">Experiencias</p>
            </div>
        </div>
    </div>
    <div class="col-sm-6 col-lg-3">
        <div class="panel media pad-all">
            <div class="media-left">
                <span class="icon-wrap icon-wrap-sm icon-circle bg-danger">
                    <i class="ti-briefcase fa-2x"></i>
                </span>
            </div>
            
            <div class="media-body">
                <p class="text-2x mar-no text-thin">{{$hotelCount}}</p>
                <p class="text-muted mar-no">Hoteles</p>
            </div>
        </div>
    </div>
</div>

<div class="row">
    <div id="graphOrder" class="col-sm-6 col-lg-12">
        
    </div>
    
</div>

@endcan  
@endsection

@section('styles')
    <style>
        /* Show in default resolution screen*/
        #graphOrder {
            height: 500px; 
            width: 100%;
        }

        /* If in mobile screen with maximum width 479px. The iPhone screen resolution is 320x480 px (except iPhone4, 640x960) */    
        @media only screen and (max-width: 479px){
            #graphOrder { 
                margin-top: 25px;
                height: 300px; 
                width: 100%; 
            
            }
        }

    </style>

@endsection

@section('scripts')

<script type="text/javascript" src="{{ asset('/js/echarts.min.js') }}"></script>

<script type="text/javascript">
  
  let actualYear = @json($actualYear);

  let dataMonthly = @json($orderMonthlyArray);

  // declaro las ordenes totales por mes


  let myChart = echarts.init(document.getElementById("graphOrder"));

  option = {
      title: {
          text: 'Cantidad de Ordenes Mensuales Año '+actualYear
      },
      tooltip: {},
      legend: {
          data:['Cantidad']
      },
      xAxis: {
          data: ["ENE","FEB","MAR","ABR","MAY","JUN", "JUL" , "AGO" , "SEP" , "OCT","NOV","DIC"]
      },
      yAxis: {},
      series: [{
          name: 'Cantidad',
          type: 'bar',
          data: [dataMonthly[0], dataMonthly[1], dataMonthly[2], dataMonthly[3], dataMonthly[4], dataMonthly[5], dataMonthly[6], dataMonthly[7],dataMonthly[8],dataMonthly[9],dataMonthly[10],dataMonthly[11]]
      }]
  };

  myChart.setOption(option);

</script>



<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.8.0/Chart.js"></script>
<script>
    function random_rgba() {
        var o = Math.round, r = Math.random, s = 255;
        return o(r()*s) + ',' + o(r()*s) + ',' + o(r()*s);
    }
</script>
@endsection