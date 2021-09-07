@extends('template.base')

@section('page-title', 'Error')

@section('content')

    <header class="section page-header page-header-2">

    </header>
    <div class="container-fluid demo"
        style="background: url('./themes/web/assets/img/bg_error.png'); background-size:cover; background-position: center; min-height:700px">

        <section class="align-middle">
            <div class="row">
                <div class="col-md-12 mt-5 py-5">
                    <div class="jumbotron bg-transparent text-left w-50 m-auto">
                        <h1 class="display-3 text-warnings font-weight-bold mb-0">ERROR</h1>
                        <p class="lead font-30 text-warnings mb-0"><strong class="font-weight-bold text-warnings">Algo ha
                                salido mal</strong> inténtalo nuevamente</p>
                        <p class="lead font-14">Si el problema persiste llámanos y te ayudaremos a la brevedad</p>
                        <a class="btn btn-success btn-lg px-4 mt-3 font-14" href="{{ route('home') }}"
                            role="button">Volver Atras</a>
                    </div>
                </div>
            </div>
        </section>

    </div>


@endsection

@section('styles')
@endsection

@section('scripts')

@endsection
