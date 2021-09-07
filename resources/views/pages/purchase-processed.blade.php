@extends('template.base')
@section('page-title', 'Compra procesada')



@section('content')



    <header class="section page-header page-header-2">

    </header>

    <div class="container-fluid demo w-xl-75 w-100">
        <section>
            {{-- cambio de margin-top: 200px a margin-top: 70px --}}
            <div class="row" style="margin-top: 70px !important">
                <div class="col-md-12">
                    {{-- quitado el display 3, reemplazado por un h3 --}}
                    <h2 class="text-warnings mb-0 font-weight-bold ml-xl-3 ml-0 text-xl-left text-center">PAGO REALIZADO CORRECTAMENTE!</h2>
                    <h5 class="text-warnings mb-0 ml-xl-3 m-0 text-xl-left text-center"><strong class="font-weight-bold">Su
                            pago con numero de pedido: {{ $unique_code }} ha sido procesada exitosamente</strong> </h5>
                </div>
            </div>
        </section>

        {{-- <section>
            <div class="container-fluid">
                <div class="row">
                    <div class="col-xl-6 col-12">
                        <p class="font-weight-bold font-18 color-3 text-xl-left text-center">Detalle del pago</p>
                    </div>
                    <div class="col-xl-6 col-12 text-xl-right text-center">


                    </div>
                </div>
            </div>
        </section> --}}

        <section>
            <div class="container-fluid">
                <div class="row mt-2">
                    <div class="col-xl-6 col-12">
                        <p class="font-weight-bold font-18 color-3 text-xl-left text-center text-dark">Detalle del pago</p>
                    </div>
                    {{-- <div class="col-xl-6 col-12 text-xl-right text-center">

                    </div> --}}
                </div>

                <div class="row mt-3 mb-5">
                    <div class="col-12">
                        <table data-toggle="table" class="table table-bordered table-hover table-sm table-condensed">
                            <thead class="bg-primary text-white">
                                <tr>
                                    <th>VALOR</th>
                                    <th>FECHA</th>
                                </tr>
                            </thead>
                            <tbody class="text-dark">
                                <tr>
                                    <td>${{ number_format($total, 0, '.', '.') }}</td>
                                    <td>{{ $order->payment_date }}</td>
                                </tr>

                            </tbody>
                        </table>
                    </div>
                </div>

                <div class="row mb-5 d-flex">
                    {{-- <div class="col-md-8">
                    <p class="font-weight-bold text-xl-left text-center"><strong>Comentario adicional</strong></p>
                    </div> --}}


                    <div class="mr-auto p-2">
                        <a href="{{ route('home') }}"
                            class="btn btn-outline-primary px-5 py-3 font-11 mt-2 p-auto ml-3">Volver a
                            Inicio</a>
                    </div>


                    <div class="p-2">
                        <p
                            class="text-center font-23 font-weight-bold text-xl-right text-center h4 text-dark mt-4 p-auto mr-3">
                            <strong>TOTAL: ${{ number_format($total, 0, ',', '.') }}</strong>
                        </p>
                    </div>

                </div>
                {{-- <div class="row liner-total">
                    <div class="col-12">
                        <p class="mb-0 p-4 text-primary text-xl-left text-center">{{ $order->comments ?? 'Sin comentarios.'}}</p>
                    </div>
                    </div> --}}
                {{-- <div class="row">
                        <div class="col-md-12 text-xl-left text-center">
                            <a href="{{ route('home') }}" class="btn btn-outline-primary px-5 py-3 font-11 mt-2">Volver a
                                Inicio</a>
                        </div>
                    </div> --}}
            </div>

        </section>

    </div><!-- container -->


@endsection

@section('styles')
@endsection

@section('scripts')
@endsection
