@extends('template.base')
@section('page-title','Amazing Geo Guide')

@section('content')
 <header class="section page-header">
      <div class="rd-navbar-wrap">
        <nav class="rd-navbar rd-navbar-modern novi-background" data-layout="rd-navbar-fixed" data-sm-layout="rd-navbar-fixed" data-md-layout="rd-navbar-fixed"
          data-md-device-layout="rd-navbar-fixed" data-lg-layout="rd-navbar-fixed" data-lg-device-layout="rd-navbar-fixed" data-xl-layout="rd-navbar-static"
          data-xl-device-layout="rd-navbar-static" data-xxl-layout="rd-navbar-static" data-xxl-device-layout="rd-navbar-static" data-lg-stick-up-offset="10px"
          data-xl-stick-up-offset="10px" data-xxl-stick-up-offset="10px" data-lg-stick-up="true" data-xl-stick-up="true" data-xxl-stick-up="true">
          <div class="rd-navbar-main">
            <div class="rd-navbar-panel"><button class="rd-navbar-toggle" data-rd-navbar-toggle=".rd-navbar-nav-wrap"><span></span></button>
              <div class="rd-navbar-brand">
                <a class="brand" href="{{route('home')}}"><img class="brand-logo-dark" src="images/logo-1.png" alt="" width="312" height="44"><img class="brand-logo-light" src="images/logo-inverse-165x32.png"
                    alt="" width="165" height="32" srcset="images/logo-inverse-324x63.png 2x"></a>
              </div>
            </div>
            <div class="rd-navbar-nav-wrap">
              <ul class="rd-navbar-nav justify-content-end">
                <li class="rd-nav-item"><a class="rd-nav-link" href="#acerca_de"><span data-novi-id="24">Acerca de</span></a></li>
                <li class="rd-nav-item"><a class="rd-nav-link" href="#guias"><span data-novi-id="25">Guías</span></a></li>
                <li class="rd-nav-item"><a class="rd-nav-link" href="#contacto"><span data-novi-id="26">Contacto</span></a></li>
                <li class="rd-nav-item"><a href="rd-nav-link">
                		
                	<div class="row w-xl-100 w-25 m-auto">
                		<div class="col-12 text-center">
                			<div class="row">
                				<div class="col-6">
                					<i class="fa fa-instagram font-23 color-fa"></i>
                				</div>
                				<div class="col-6 text-left">
                					<i class="fa fa-facebook font-23 color-fa"></i>
                				</div>
                			</div>
                		</div>
                	</div>

                </a></li>
                <li class="rd-nav-item d-xl-none d-lg-block d-md-block d-block mt-3">
                	<a class="rd-nav-link" href="#contacto"><span data-novi-id="26">Descarga la app</span></a>
                </li>

                <li class="rd-nav-item d-xl-none d-lg-block d-md-flex d-flex mt-3">
                	<div class="row m-auto">
	                  <div class="col-6 text-right"><img class="border-white" src="images/google-1.png" alt="" width="125"></div>
	                  <div class="col-6 text-left"><img class="border-white" src="images/app-1.png" alt="" width="125"></div>
	                </div>

                </li>
                
              </ul>
            </div>
            <div class="rd-navbar-element bg-accent"><a class="button button-sm button-header button-winona text-white" href="#">Descarga la App</a></div>
            <div class="rd-navbar-dummy"></div>
          </div>
        </nav>
      </div>
    </header>
    <section class="section parallax-container section-md bg-accent" data-parallax-img="images/4.-estratos-inclinados-3.png" id="about-us">
      <div class="parallax-content p-5">
        <div class="container">
          <div class="row row-50 justify-content-end">
            <div class="col-xl-4 text-center"><img src="images/grupo-115.png" alt="" width="400"></div>
            <div class="col-xl-8 text-center">
              <div class="block-5 wow clipInLeft mt-4">
                <h3 class="wow clipInLeft" data-wow-delay=".1s"><span></span><span></span><span data-novi-id="13">Explora la increíble geología de Chile a través de Inland</span></h3>
                <p class="big wow clipInLeft inset-3"
                  data-wow-delay=".2s" data-novi-id="14"><span data-novi-id="15">Planifica, descubre &amp; comparte.</span></p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section class="section novi-background bg-cover" style="background-color: rgb(255, 255, 255);">
      <div class="container" id="acerca_de">
        <div class="row align-items-end justify-content-center">
          <div class="col-md-10 col-lg-6">
          
              <h3 class="font-54 text-center mt-xl-0 mt-4">Comienza a vivir tu<br> <strong>#experienciainland</strong></h3>
             
              <p class="text-gray-900" data-novi-id="8"><span data-novi-id="9">Inland es un tour guiado digital que tendrás siempre disponible desde tu celular con la flexibilidad y al precio de una App.<br data-novi-id="11"><br data-novi-id="10"> Un mapa georeferenciado disponible offline te guía en todo tu recorrido.</span></p>
              <div
                class="row">
                <div class="col-6 text-right"><img src="images/google-1.png" alt="" width="157" height="51"></div>
                <div class="col-6 text-left"><img src="images/app-1.png" alt="" width="155"></div>
            </div>
          
        </div>
        <div class="col-md-10 col-lg-6 text-center"><img src="images/mobile.png" alt="" width="600" height="570"></div>
      </div>
      <div class="row mt-5 mb-5">
        <div class="col-12 text-center"><img src="images/grupo-62.png" alt="" width="621" height="19"></div>
      </div>
  </div>
  </section>
  <section class="section section-md text-center bg-accent novi-background bg-cover" id="media" style="background-color: rgb(247, 247, 247);">
    <div class="container">
      <h3 class=""><span data-novi-id="0"><span data-novi-id="12">Te apoya</span> en todas las etapas de tu viaje</span>
      </h3>
      <div class="row">
        @forelse ($steps as $stepItem)
          <div class="col-xl-4 col-lg-4 col-md-6">
            <div class="wow clipInLeft" data-wow-delay=".2s">
              <a class="link-image-2" href="//{{$stepItem->href_button}}"><img src="{{ $stepItem->public_image }}" alt="" width="114" height="114"></a>
            </div>
            <p><span data-novi-id="1">{!! $stepItem->description !!}</span></p>
          </div>
            
        @empty
            
        @endforelse

        {{-- <div class="col-xl-4 col-lg-4 col-md-6">
          <div class="wow clipInLeft" data-wow-delay=".3s">
            <a class="link-image-2" href="#"><img src="images/1.png" alt="" width="114" height="114"></a>
          </div>
          <p><span data-novi-id="2">Mientras recorres tu destino, con impactante información sobre los sitios que ves. </span></p>
        </div>
        <div class="col-xl-4 col-lg-4 col-md-6">
          <div class="wow clipInLeft" data-wow-delay=".4s">
            <a class="link-image-2" href="#"><img src="images/3.png" alt="" width="114" height="114"></a>
          </div>
          <p class=""><span data-novi-id="3">Hasta que vuelves a tu hogar y compartes tu experiencia con tu familia y amigos, o buscas inspiración para una nueva aventura.</span></p>
        </div> --}}
      </div>
    </div>
  </section>
  <section class="section section-md bg-gray-100 text-center novi-background bg-cover" style="background-color: rgb(255, 255, 255);">
    <div class="container">
      <h3 class="wow fadeIn"><span data-novi-id="19"><span data-novi-id="4">Beneficios</span> de usar la app</span>
      </h3>
      <div class="row row-30 row-xl-60">
        @forelse ($benefits as $benefitItem)
          <div class="col-sm-6 col-lg-4">
            <article class="box-modern wow fadeIn novi-background" data-anime="circles-2" style="background-color: rgb(247, 247, 247);">
              <div class="box-modern-media text-xl-right text-center"><img src="{{ $benefitItem->public_image }}" alt="" width="36" height="36"></div>
              <p class="box-modern-title"><span data-novi-id="27">{{$benefitItem->title}}</span></p>
              <div class="box-modern-text">
                <p class=""><span data-novi-id="33">{!! $benefitItem->description !!}</span></p>
              </div>
            </article>
          </div>
            
        @empty
            
        @endforelse

        {{-- <div class="col-sm-6 col-lg-4">
          <article class="box-modern wow fadeIn novi-background" data-anime="circles-2" style="background-color: rgb(247, 247, 247);">
            <div class="box-modern-media text-xl-right text-center"><img src="images/alfiler.png" alt="" width="36" height="36"></div>
            <p class="box-modern-title"><span data-novi-id="28">Georeferenciación</span></p>
            <div class="box-modern-text">
              <p class=""><span data-novi-id="34">Comparte tu #experienciaInland e interactúa con otros viajeros que inspiran tu próxima aventura </span></p>
            </div>
          </article>
        </div>
        <div class="col-sm-6 col-lg-4">
          <article class="box-modern wow fadeIn novi-background" data-anime="circles-2" style="background-color: rgb(247, 247, 247);">
            <div class="box-modern-media text-xl-right text-center"><img src="images/trazado-260.png" alt="" width="36" height="36"></div>
            <p class="box-modern-title"><span data-novi-id="29">Geología</span></p>
            <div class="box-modern-text">
              <p><span data-novi-id="35">¿No sabes lo que necesitas llevar a tu nueva aventura? Nosotros te aconsejamos</span></p>
            </div>
          </article>
        </div>
        <div class="col-sm-6 col-lg-4">
          <article class="box-modern wow fadeIn novi-background" data-anime="circles-2" style="background-color: rgb(247, 247, 247);">
            <div class="box-modern-media text-xl-right text-center"><img src="images/icon-ionic-ios-information-circle-outline.png" alt="" width="36" height="36"></div>
            <p class="box-modern-title"><span data-novi-id="30">Información de</span></p>
            <div class="box-modern-text">
              <p class=""><span data-novi-id="36">Para que sea más fácil desenvolverte de manera independiente, contarás con detalle de las rutas que escojas recorrer: dificultad, altimetría y tiempos promedio de recorrido</span></p>
            </div>
          </article>
        </div>
        <div class="col-sm-6 col-lg-4">
          <article class="box-modern wow fadeIn novi-background" data-anime="circles-2" style="background-color: rgb(247, 247, 247);">
            <div class="box-modern-media text-xl-right text-center"><img src="images/sharing.png" alt="" width="36" height="36"></div>
            <p class="box-modern-title"><span data-novi-id="31">Comunidad</span></p>
            <div class="box-modern-text">
              <p><span data-novi-id="37">Un mapa georreferenciado disponible offline te guiará en tu recorrido, mostrándote tu ubicación en tiempo real, y la de los sitios de interés</span></p>
            </div>
          </article>
        </div>
        <div class="col-sm-6 col-lg-4">
          <article class="box-modern wow fadeIn novi-background" data-anime="circles-2" style="background-color: rgb(247, 247, 247);">
            <div class="box-modern-media text-xl-right text-center"><img src="images/mochila.png" alt="" width="36" height="36"></div>
            <p class="box-modern-title"><span data-novi-id="32">Equipos</span></p>
            <div class="box-modern-text">
              <p><span data-novi-id="38">En tu recorrido, podrás comprender los procesos de millones de años que dan forma al paisaje ¿Por qué los diferentes colores en las rocas? ¿Cómo se forma un volcán, un fósil o un glaciar?</span></p>
            </div>
          </article>
        </div> --}}
      </div>
    </div>
  </section>
  <section class="section section-md text-center bg-white novi-background bg-cover" style="background-color: #f7f7f7!important;">
    <div class="container">
      <h3 id="guias"><span data-novi-id="20"><span data-novi-id="17">Nuestras </span>guías</span>
      </h3>
      <div class="owl-carousel owl-carousel_profile-modern" data-items="2" data-sm-items="2" data-lg-items="4" data-xl-items="5" data-dots="false" data-nav="true"
        data-stage-padding="0" data-loop="false" data-margin="30" data-mouse-drag="false">
        @forelse ($guides as $guideItem)
          <article class="profile-modern">
            <figure class="profile-modern-figure"><img class="profile-modern-image" src="{{$guideItem->public_image}}" alt="" width="369" height="315"></figure>
          </article>
        @empty
            
        @endforelse
        
        {{-- <article class="profile-modern">
          <figure class="profile-modern-figure"><img class="profile-modern-image" src="images/torres-1.png" alt="" width="369" height="315"></figure>
        </article>
        <article class="profile-modern">
          <figure class="profile-modern-figure"><img class="profile-modern-image" src="images/sanpedro.png" alt="" width="369" height="315"></figure>
        </article>
        <article class="profile-modern">
          <figure class="profile-modern-figure"><img class="profile-modern-image" src="images/isla.png" alt="" width="369" height="315"></figure>
        </article>
        <article class="profile-modern">
          <figure class="profile-modern-figure"><img class="profile-modern-image" src="images/araucania.png" alt="" width="369" height="315"></figure>
        </article> --}}
      </div>
    </div>
  </section>
  <section class="section section-md bg-gray-100 novi-background bg-cover" style="background-color: rgb(255, 255, 255);">
    <div class="container">
      <h3 class="text-center" id="contacto"><span data-novi-id="18">Contáctanos</span></h3>
      <div class="row justify-content-center row-fix">
        <div class="col-lg-11 col-xl-9">
          {{-- FORMULARIO   --}}
          
          <form class="rd-mailform rd-form" id="form-contact" data-form-output="form-output-global" data-form-type="contact">
            @csrf
            <div class="row row-x-16 row-20 row-fix">
              <div class="col-md-6">
                <div class="form-wrap"><input class="form-input" id="contact-name" type="text" name="name" data-constraints="@Required"><label class="form-label" for="contact-name">Nombre</label></div>
              </div>
              <div class="col-md-6">
                <div class="form-wrap"><input class="form-input" id="contact-last-name" type="text" name="last_name" data-constraints="@Required @Email"><label class="form-label" for="contact-email">Apellido</label></div>
              </div>
              <div class="col-md-6">
                <div class="form-wrap"><input class="form-input" id="contact-email" type="email" name="email" data-constraints="@Required"><label class="form-label" for="contact-name">Email</label></div>
              </div>
              <div class="col-md-6">
                <div class="form-wrap"><input class="form-input" id="contact-email" type="text" name="phone" data-constraints="@Required @Email"><label class="form-label" for="contact-email">Teléfono</label></div>
              </div>
              <div class="col-12">
                <div class="form-wrap"><label class="form-label" for="contact-message">Mensaje</label><textarea class="form-input" id="contact-message" name="description" data-constraints="@Required"></textarea></div>
              </div>
              <div class="col-md-12 text-center">
                <div class="form-wrap form-button"><button class="button button-primary" type="button" onclick="doForm();"><span data-novi-id="21">Enviar</span></button></div>
              </div>
            </div>
          </form>
        
        
        </div>
      </div>
    </div>
  </section>
  <section class="section novi-background bg-cover" style="background-color: #f7f7f7;">
    <div class="container">
      <div class="row align-items-end justify-content-center">
        <div class="col-md-10 col-lg-12 text-center">
          <h3 class="mt-5 mb-4"><span data-novi-id="22"><span data-novi-id="23">Síguenos</span> en nuestras redes</span>
          </h3>
        </div>
        <div class="row mb-5 justify-content-center">
          <div class="col-md-10 col-lg-6 text-xl-right text-md-center text-lg-center text-center"><a href="#"><img src="images/instagram.png" alt="" width="394" height="226"></a></div>
          <div class="col-md-10 col-lg-6 text-xl-left text-md-center text-lg-center text-center"><a href="#"><img src="images/facebook.png" alt="" width="394" height="226"></a></div>
        </div>
      </div>
    </div>
  </section>
  <footer class="section footer-classic novi-background bg-cover" style="background-color: rgb(2, 2, 2);">
    <div class="footer-classic-main">
      <div class="container">
        <div class="row row-50 justify-content-lg-between">
          <div class="col-md-12 col-lg-3 col-xl-6 text-xl-left text-center">
            <a class="brand" href="{{route('home')}}"><img class="brand-logo-dark" src="images/logo-app-4.png" alt="" width="312" height="44"></a>
          </div>
          <div class="col-md-12 col-lg-3 col-xl-6">
            <div class="row">
              <div class="col-xl-6 col-lg-6 col-md-12">
                <div class="row mt-4">
                  <div class="col-6 text-right"><a href="#"><img class="border-white" src="images/google-1.png" alt="" width="125"></a></div>
                  <div class="col-6 text-left"><a href="#"><img class="border-white" src="images/app-1.png" alt="" width="125"></a></div>
                </div>
              </div>
              <div class="col-xl-6 col-lg-6 col-md-12 text-xl-left text-center mt-xl-0 mt-5"><a href="#"><img class="brand-logo-dark" src="images/unnamed-2.png" alt="" width="246" height="85"></a></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </footer>
@endsection

@section('scripts')
<script>

  let urlForm = '{{ route('sendemailcontact') }}';

  function doForm() {
    
      var data = new FormData();

      //Form data
      var form_data = $('#form-contact').serializeArray();
      $.each(form_data, function (key, input) {
          data.append(input.name, input.value);
      });

      $.ajax({
          type: "POST",
          url: urlForm,
          data: data,
          processData: false,
          contentType: false,
          success: function (response) {
          
          if(response.status=='success')
          {
              swal({
                  title: 'Correo Enviado',
                  html: 'Se le respondera en el correo indicado',
                  type: 'success',
                  showCancelButton: false,
                  confirmButtonColor: '#43a047',
                  cancelButtonColor: '#d33',
                  confirmButtonText: 'Aceptar',
                  cancelButtonText: 'No, cancelar!'
              }).then(function (result) {
                  
              });
          }
          else if (response.status=='error')
          {
              swal({
                  title: '!Error Inesperado¡',
                  html: 'Intente mas tarde',
                  type: 'error',
                  showCancelButton: false,
                  confirmButtonColor: '#43a047',
                  cancelButtonColor: '#d33',
                  confirmButtonText: 'Aceptar',
                  cancelButtonText: 'No, cancelar!'
              }).then(function (result) {
                  
              });
          }
          else if (response.status=='validate')
          {
              swal({
                  title: 'Campos Incompletos',
                  html: 'Complete todos los campos',
                  type: 'error',
                  showCancelButton: false,
                  confirmButtonColor: '#43a047',
                  cancelButtonColor: '#d33',
                  confirmButtonText: 'Aceptar',
                  cancelButtonText: 'No, cancelar!'
              }).then(function (result) {
                  
              });
          }
          
          },
          
          error : function(error){
              simpleAlert('¡Error!', error.responseJSON.message, 'danger', '.alert-simple-login', true);
          }
      });
  }
</script> 
@endsection