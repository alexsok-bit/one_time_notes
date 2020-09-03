function secure_show(url, csrf) {
    if (confirm('Show now?')) {
        get_snippet(url, csrf)
    } else {
        console.log('Thing was not saved to the database.');
    }
}


function get_snippet(url, csrf) {
    const oReq = new XMLHttpRequest();
    oReq.onload = reqListener;
    oReq.open("post", url, false);
    oReq.withCredentials = true;
    oReq.setRequestHeader("Content-Type", 'application/x-www-form-urlencoded');
    oReq.setRequestHeader("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8");
    oReq.setRequestHeader("Upgrade-Insecure-Requests", "1");
    oReq.send("csrfmiddlewaretoken=" + csrf);
}


function reqListener () {
    link.remove();
    show_actions.remove();

    save_action.style.display = "";
    text.style.display = "";
    text.value = this.responseText;
}


function xclip() {
    const textArea = document.createElement("textarea");
    textArea.style.position = 'fixed';
    textArea.style.top = '0';
    textArea.style.left = '0';
    textArea.style.width = '2em';
    textArea.style.height = '2em';
    textArea.style.padding = '0';
    textArea.style.border = 'none';
    textArea.style.outline = 'none';
    textArea.style.boxShadow = 'none';
    textArea.style.background = 'transparent';
    textArea.value = link.innerText;
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();
    try {
        const successful = document.execCommand('copy');
        const msg = successful ? 'successful' : 'unsuccessful';
        console.log('Copying text command was ' + msg);
    } catch (err) {
        console.log('Oops, unable to copy');
    }
    document.body.removeChild(textArea);
}
