function check_tos_accepted() {
    if (document.getElementById('agree-tos-checkbox').checked) {
        document.getElementById('agree-tos-error').classList.add("hidden");
        return true
    }
    else {
        document.getElementById('agree-tos-error').classList.remove("hidden");
        return false
    }
}

window.onload = function(){
    var browser_recommondation = " For the best experience we recommend to use the latest Chrome or Firefox as browser. For Internet Explorer only IE11 is supported.";
    var browser_not_supported = "Your current browser doesn't support some features required for our app.";
    var browser_maybe_supported = "Your seem to use an not supported browser. Our app might not work correctly with this browser.";
    var warning_header = '<h4 class="browser-warn-header">Please note</h4> ';
    var cb = check_browser();
    // 0: not supported  1: maybe  2: supported
    if ( cb == 0 ) {
        document.getElementById('browser-warning').innerHTML =  warning_header + browser_not_supported + browser_recommondation
    }
    else if ( cb == 1 ){
        document.getElementById('browser-warning').innerHTML = warning_header + browser_maybe_supported + browser_recommondation
    }

    if ( document.getElementById('page-overlay') ) {
        document.getElementById('page-overlay').addEventListener('click', function () {
            document.getElementById('page-overlay').classList.add('hidden');
            document.getElementById('page-overlay-content').classList.add('hidden');
        })
    }

    var lightbox = new Lightbox();
    lightbox.load();

    if (window.run_example_anim) {
        run_example_anim()
    }

};

function randomIntFromInterval(min,max)
{
    return Math.floor(Math.random()*(max-min+1)+min);
}

function show_waiting_spinner() {
    document.body.insertAdjacentHTML( 'afterbegin', '<div id="myID">...</div>' );
}