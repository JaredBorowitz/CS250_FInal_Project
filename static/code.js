function updateNmap() {
    address = document.getElementById('address').value;
    sv = document.getElementById('sv').checked ? "-sV" : "";
    sc = document.getElementById('sc').checked ? "-sC" : "";
    su = document.getElementById('su').checked ? "-sU" : "";
    so = document.getElementById('so').checked ? "-sO" : "";

    port = getPortString();
    tSlide = getTSlider();

    var nmap_string = 'nmap ';

    nmap_string = "nmap" + sv + " " + sc + " " + su + " " + so + " " + port + " " + tSlide + " " + address;

    console.log(nmap_string);

    document.getElementById('preview').innerHTML = nmap_string;
}
function getPortString() {
    pCheck = document.getElementById('p_check');

    if(!pCheck.checked) {
        return "";
    }

    all_ports = document.getElementById('p_all');
    one_port = document.getElementById('p_one');
    range_ports = document.getElementById('p_range');

    if(all_ports.checked) {
        return "-p-";
    }
    if(one_port.checked) {
        port_num = document.getElementById('p_one_num').value;
        if (port_num) {
            return "-p " + port_num;
        }
    }
    if(range_ports.checked) {
        start = document.getElementById('p_rng_str').value;
        end = document.getElementById('p_rng_end').value;
        if(start && end) {
            return "-p " + start + "-" + end;
        }
    }
    return "";
}
function getTSlider() {
    tCheck = document.getElementById('t_speed');
    if(!tCheck.checked) {
        return "";
    }
    t_value = document.getElementById('t_num').value;
    if(t_value==="") {
        return "";
    }
    else {
        return "-T" + t_value;
    }

}
function openOptions() {
    options = document.getElementById('cmd_options');

    if(options.hidden) {
        options.hidden = !options.hidden;
    }
}
function openPorts() {
    port1 = document.getElementById('port1');
    port2 = document.getElementById('port2');
    port3 = document.getElementById('port3');

    port1.hidden = !port1.hidden;
    port2.hidden = !port2.hidden;
    port3.hidden = !port3.hidden;

}
function openPort1() {
    p_one_num = document.getElementById('p_one_num');
    start = document.getElementById('p_rng_str');
    end = document.getElementById('p_rng_end');

    if(p_one_num.hidden) {
        p_one_num.hidden = !p_one_num.hidden;
    }
    if(!start.hidden && !end.hidden) {
        start.hidden = !start.hidden;
        end.hidden = !end.hidden;
    }
}
function openPort2() {
    start = document.getElementById('p_rng_str');
    end = document.getElementById('p_rng_end');
    p_one_num = document.getElementById('p_one_num');

    if(start.hidden && end.hidden) {
        start.hidden = !start.hidden;
        end.hidden = !end.hidden;
    }
    if(!p_one_num.hidden) {
        p_one_num.hidden = !p_one_num.hidden;
    }
}
function openTSpeed() {
    t_slider = document.getElementById('t_slider');

    t_slider.hidden = !t_slider.hidden;

    adjustT();
}
function adjustT() {
    t_print = document.getElementById('t_range');
    t_num = document.getElementById('t_num').value;
    t_print.innerHTML = t_num;

    updateNmap();
}