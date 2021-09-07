@extends('emails.base_email')

@section('content')
<div class="titulo text-primary">Contacto:</div>
<div class="mensaje">  
    Nombre: <b> {{$name ?? ""}}</b>.
    <br/>
    Apellido: <b> {{$last_name ?? ""}}</b>.
    <br/>
    Correo: {{$email ?? ""}}.
    <br/>
    Telefono: {{$phone ?? ""}}.
    <br/>
    Mensaje: {{$description ?? ""}}
</div>
<div class="text-legal">
    Este mensaje ha sido enviado automáticamente, por favor no responder este email.
    <br><br>
</div>
@endsection