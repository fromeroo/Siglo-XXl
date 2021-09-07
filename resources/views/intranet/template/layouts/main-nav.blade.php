<nav id="mainnav-container">
    <div id="mainnav">


        <!--Menu-->
        <!--================================-->
        <div id="mainnav-menu-wrap">
            <div class="nano">
                <div class="nano-content">

                    <!--Profile Widget-->
                    <!--================================-->
                    <div id="mainnav-profile" class="mainnav-profile">
                        <div class="profile-wrap text-center">
                            <div class="pad-btm">
                                @if(file_exists(storage_path('app/public/perfil/'.auth()->user()->id.'.jpg')) || file_exists(storage_path('app/public/perfil/'.auth()->user()->id.'.png')))
                                    @if(file_exists(storage_path('app/public/perfil/'.auth()->user()->id.'.jpg')))
                                        <img class="img-circle img-md" id="image-product" src="{{ Storage::url('public/perfil/'.auth()->user()->id.'.jpg') }}">
                                    @else
                                        <img class="img-circle img-md" id="image-product" src="{{ Storage::url('public/perfil/'.auth()->user()->id.'.png') }}">
                                    @endif
                                @else
                                    <img class="img-circle img-md" src="/themes/intranet/img/user-default.png"
                                     alt="Profile Picture">
                                @endif
                            </div>
                            <a href="#profile-nav" class="box-block" data-toggle="collapse" aria-expanded="false">
                                            <span class="pull-right dropdown-toggle">
                                                <i class="dropdown-caret"></i>
                                            </span>
                                <p class="mnp-name">{{ auth()->guard('intranet')->user()->full_name }}</p>
                                <span class="mnp-desc">{{ auth()->guard('intranet')->user()->email }}</span>
                            </a>
                        </div>
                        <div id="profile-nav" class="collapse list-group bg-trans">
                            <a href="{{ route('intranet.profile.editProfile') }}" class="list-group-item">
                                <i class="demo-pli-male icon-lg icon-fw"></i> Ver Perfil
                            </a>
                            <a href="{{ route('intranet.auth.logout') }}" class="list-group-item">
                                <i class="demo-pli-unlock icon-lg icon-fw"></i> Salir
                            </a>
                        </div>
                    </div>

                    <ul id="mainnav-menu" class="list-group" style="margin-bottom: 120px;">
                        <li class="treeview {{ is_parent_menu_active(['intranet/inicio', 'intranet/administradores', 'intranet/clientes', 'intranet/ordenes', 'intranet/roles',
                            'intranet/hoteles', 'intranet/configuracion-invitaciones', 'intranet/listado-favoritos-clientes', 'intranet/invitaciones']) }}">
                                <a href="#">
                                    <i class="list-header"></i>
                                    <span class="menu-title">ADMIN</span>
                                    <i class="arrow"></i>
                                </a>
                            <!--Submenu-->
                            <ul class="collapse">
                                @can('intranet.dashboard')
                                <li class="{{ is_menu_active('intranet/inicio') }}">
                                    <a href="{{ route('intranet.dashboard') }}">
                                        <i class="ti-home"></i>
                                        <span class="menu-title">Inicio</span>
                                    </a>
                                </li>
                                @endcan 

                                
                                @can('intranet.users.index')
                                <li class="{{ is_menu_active('intranet/administradores') }}">
                                    <a href="{{ route('intranet.users.index') }}">
                                        <i class="ti-user"></i>
                                        <span class="menu-title">Administradores</span>
                                    </a>
                                </li>
                                @endcan

                                @can('intranet.roles.index')
                                <li class="{{ is_menu_active('intranet/roles') }}">
                                    <a href="{{ route('intranet.roles.index') }}">
                                        <i class="ti-key"></i>
                                        <span class="menu-title">Roles</span>
                                    </a>
                                </li>
                                @endcan

                                @can('intranet.clients.index')
                                <li class="{{ is_menu_active('intranet/clientes') }}">
                                    <a href="{{ route('intranet.clients.index') }}">
                                        <i class="ti-face-smile"></i>
                                        <span class="menu-title">Clientes</span>
                                    </a>
                                </li>
                                @endcan

                                @can('intranet.orders.index')
                                <li class="{{ is_menu_active('intranet/ordenes') }}">
                                    <a href="{{ route('intranet.orders.index') }}">
                                        <i class="ti-location-arrow"></i>
                                        <span class="menu-title">Ordenes de compra</span>
                                    </a>
                                </li>
                                @endcan

                                @can('intranet.hotels.index')
                                <li class="{{ is_menu_active('intranet/hoteles') }}">
                                    <a href="{{ route('intranet.hotels.index') }}">
                                        <i class="ti-briefcase"></i>
                                        <span class="menu-title">Empresas</span>
                                    </a>
                                </li>
                                @endcan

                                @can('intranet.settings.index')
                                <li class="{{ is_menu_active('intranet/configuracion-invitaciones') }}">
                                    <a href="{{ route('intranet.settings.index') }}">
                                        <i class="ti-bookmark-alt"></i>
                                        <span class="menu-title">Configuración Invitaciones Empresas</span>
                                    </a>
                                </li>
                                @endcan

                                @if (auth()->guard('intranet')->user()->hasRole('Empresa'))
    
                                    @can('intranet.invitations.index')
                                        <li class="{{ is_menu_active('intranet/invitaciones') }}">
                                            <a href="{{ route('intranet.invitations.index') }}">
                                                <i class="ti-bookmark-alt"></i>
                                                <span class="menu-title">Invitaciones Empresas</span>
                                            </a>
                                        </li>
                                    @endcan
                                    
                                @endif

                                @can('intranet.favorites.index')
                                <li class="{{ is_menu_active('intranet/listado-favoritos-clientes') }}">
                                    <a href="{{ route('intranet.favorites.index') }}">
                                        <i class="ti-bookmark-alt"></i>
                                        <span class="menu-title">Favoritos</span>
                                    </a>
                                </li>
                                @endcan

                            </ul>
                        </li>
                        <li class="treeview {{ is_parent_menu_active(['intranet/guias', 'intranet/regiones', 'intranet/zonas', 'intranet/areas',
                            'intranet/lugares', 'intranet/geomarcadores', 'intranet/trekkings', 'intranet/categorias-geomarcador']) }}">
                            @if (!auth()->guard('intranet')->user()->hasRole('Empresa'))
                                <a href="#">
                                    <i class="list-header"></i>
                                    <span class="menu-title">GUÍAS</span>
                                    <i class="arrow"></i>
                                </a>
                            @endif
                            <!--Submenu-->
                            <ul class="collapse">
                                @can('intranet.guides.index')
                                <li class="{{ is_menu_active('intranet/guias') }}">
                                    <a href="{{ route('intranet.guides.index') }}">
                                        <i class="ti-notepad"></i>
                                        <span class="menu-title">Guía</span>
                                    </a>
                                </li>
                                @endcan

                                @can('intranet.regions.index')
                                <li class="{{ is_menu_active('intranet/regiones') }}">
                                    <a href="{{ route('intranet.regions.index') }}">
                                        <i class="ti-map-alt"></i>
                                        <span class="menu-title">Región</span>
                                    </a>
                                </li>
                                @endcan

                                @can('intranet.zones.index')
                                <li class="{{ is_menu_active('intranet/zonas') }}">
                                    <a href="{{ route('intranet.zones.index') }}">
                                        <i class="ti-location-pin"></i>
                                        <span class="menu-title">Zona</span>
                                    </a>
                                </li>
                                @endcan

                                @can('intranet.areas.index')
                                <li class="{{ is_menu_active('intranet/areas') }}">
                                    <a href="{{ route('intranet.areas.index') }}">
                                        <i class="ti-map-alt"></i>
                                        <span class="menu-title">Area</span>
                                    </a>
                                </li>
                                @endcan

                                @can('intranet.places.index')
                                <li class="{{ is_menu_active('intranet/lugares') }}">
                                    <a href="{{ route('intranet.places.index') }}">
                                        <i class="ti-direction"></i>
                                        <span class="menu-title">Lugar</span>
                                    </a>
                                </li>
                                @endcan

                                @can('intranet.geomarkercategories.index')
                                <li class="{{ is_menu_active('intranet/categorias-geomarcador') }}">
                                    <a href="{{ route('intranet.geomarkercategories.index') }}">
                                        <i class="ti-location-arrow"></i>
                                        <span class="menu-title">Categoría Geo Marcardor</span>
                                    </a>
                                </li>
                                @endcan

                                @can('intranet.trekkings.index')
                                <li class="{{ is_menu_active('intranet/trekkings') }}">
                                    <a href="{{ route('intranet.trekkings.index') }}">
                                        <i class="ti-image"></i>
                                        <span class="menu-title">Trekking</span>
                                    </a>
                                </li>
                                @endcan

                            </ul>                                    
                        </li>        
                        <li class="treeview {{ is_parent_menu_active(['intranet/tipos-de-equipamientos', 'intranet/items-equipamientos', 'intranet/comentarios', 'intranet/experiencias']) }}">
                            @if (!auth()->guard('intranet')->user()->hasRole('Empresa'))
                                <a href="#">
                                    <i class="list-header"></i>
                                    <span class="menu-title">EXPERIENCIAS Y</span>
                                    <span style="margin-left: 5%;" class="menu-title">EQUIPAMIENTO</span>
                                    <i class="arrow"></i>
                                </a>
                            @endif
                            <!--Submenu-->
                            <ul class="collapse">
                                @can('intranet.equipmentTypes.index')
                                <li class="{{ is_menu_active('intranet/tipos-de-equipamientos') }}">
                                    <a href="{{ route('intranet.equipmentTypes.index') }}">
                                        <i class="ti-notepad"></i>
                                        <span class="menu-title">Tipos de Equipamientos</span>
                                    </a>
                                </li>
                                @endcan

                                @can('intranet.equipmentItems.index')
                                <li class="{{ is_menu_active('intranet/items-equipamientos') }}">
                                    <a href="{{ route('intranet.equipmentItems.index') }}">
                                        <i class="ti-package"></i>
                                        <span class="menu-title">Equipamiento</span>
                                    </a>
                                </li>
                                @endcan

                                @can('intranet.comments.index')
                                <li class="{{ is_menu_active('intranet/experiencias/index') }}">
                                    <a href="{{ route('intranet.comments.index') }}">
                                        <i class="ti-comments"></i>
                                        <span class="menu-title">Experiencias</span>
                                    </a>
                                </li>
                                @endcan

                            </ul>    
                        </li>
                        <li class="treeview {{ is_parent_menu_active(['intranet/publicaciones']) }}">
                            @if (!auth()->guard('intranet')->user()->hasRole('Empresa'))    
                                <a href="#">            
                                    <i class="list-header"></i>
                                    <span class="menu-title">PUBLICACIONES</span>
                                    <i class="arrow"></i>
                                </a>
                            @endif
                            <!--Submenu-->
                            <ul class="collapse">
                                @can('intranet.posts.index')
                                <li class="{{ is_menu_active('intranet/publicaciones') }}">
                                    <a href="{{ route('intranet.posts.index') }}">
                                        <i class="ti-agenda"></i>
                                        <span class="menu-title">Publicaciones</span>
                                    </a>
                                </li>
                                @endcan

                            </ul>    
                        </li>        
                        <li class="treeview {{ is_parent_menu_active(['intranet/etapas-viaje', 'intranet/beneficios']) }}">    
                            @if (!auth()->guard('intranet')->user()->hasRole('Empresa'))
                                <a href="#">
                                    <i class="list-header"></i>
                                    <span class="menu-title">LANDING</span>
                                    <i class="arrow"></i>
                                </a>
                            @endif
                            <!--Submenu-->
                            <ul class="collapse">
                                @can('intranet.steps.index')
                                <li class="{{ is_menu_active('intranet/etapas-viaje') }}">
                                    <a href="{{ route('intranet.steps.index') }}">
                                        <i class="ti-menu-alt"></i>
                                        <span class="menu-title">Etapas del Viaje</span>
                                    </a>
                                </li>
                                @endcan

                                @can('intranet.benefits.index')
                                <li class="{{ is_menu_active('intranet/beneficios') }}">
                                    <a href="{{ route('intranet.benefits.index') }}">
                                        <i class="ti-stats-up"></i>
                                        <span class="menu-title">Beneficios</span>
                                    </a>
                                </li>
                                @endcan

                            </ul>
                        </li>         

                    </ul>
                </div>
            </div>
        </div>
        <!--================================-->
        <!--End menu-->

    </div>
</nav>

