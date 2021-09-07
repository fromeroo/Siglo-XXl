@extends('intranet.emails.base_email')

@section('content')
<div class="titulo">Estimado/a {{ $nombre }}:</div>
<div class="mensaje">
    {!! $texto !!}
</div>
<div class="text-legal">
    Este mensaje ha sido enviado automáticamente, por favor no responder este email.
    <br><br>
</div>
@endsection