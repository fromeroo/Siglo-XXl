<?php

namespace App\Http\Controllers\Intranet;

use App\Models\Ticket;
use Illuminate\Http\Request;
use App\Http\Controllers\Controller;
use Jenssegers\Date\Date;
use Carbon\Carbon;
use App\Models\Report;
use App\Models\Store;
use App\Models\User;

class DashboardController extends Controller
{
    private $route = 'intranet.';
    public $folder = 'intranet.modules.dashboard.';

    function index(Request $request)
    {
        return view($this->folder . 'index');
    }

}
