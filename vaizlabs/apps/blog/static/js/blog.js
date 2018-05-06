function focusOnImage(id, src, txt) {
    document.getElementById('gallery_'+id).src = src;
    document.getElementById('gallery_'+id).alt = txt;
}

