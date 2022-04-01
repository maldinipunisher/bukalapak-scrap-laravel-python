<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Symfony\Component\Process\Exception\ProcessFailedException;
use Symfony\Component\Process\Process;

class TaskController extends Controller
{
    public function index()
    {
        return response('Please add parameter example http://127.0.0.1:8000/api/search?q=ram', 302);
    }

    public function search(Request $request)
    {
        if (!$request->q) {
            return $this->index();
        }

        $q = $request->q;
        $process = new Process(['python', __DIR__ . '../../../../resources/plugins/api_scrapping_from_web.py', $q]);
        $process->run();

        if (!$process->isSuccessful()) {
            throw new ProcessFailedException($process);
        }
        $result = $process->getOutput();
        // dd($result);
        $decoded_result =  json_decode($result);
        return response()->json($decoded_result, 200);
    }
}
