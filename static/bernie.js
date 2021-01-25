document.addEventListener('DOMContentLoaded', () => {
    const bernieImageEl = document.getElementById('bernie-src');
    const imageOut = document.getElementById('image-out');
    const locationImgEl = document.getElementById('location-img');
    const formEl = document.getElementById('form');
    const canvasEl = document.getElementById('canvas');
    const downloadButtonEl = document.getElementById('download');
    let bernieImageHeight = 0;
    let bernieImageWidth = 0;
    let drawingContext = null;
    let mousedDown = false;

    const draw = (x=400, y=330) => {
      if (!drawingContext) {
        drawingContext = canvasEl.getContext('2d');
      }
      canvasEl.width = locationImgEl.width;
      canvasEl.height = locationImgEl.height;
      drawingContext.drawImage(locationImgEl, 0, 0)
      drawingContext.drawImage(bernieImageEl, x, y);
    }

    const downloadBernie = () => {
      const dataUrl = canvasEl.toDataURL('image/jpeg');
      const a  = document.createElement('a');
      a.href = dataUrl;
      const location = document.getElementById('location-input').value
      a.download = `bernie-${location}.jpeg`;
      a.click()
    }

    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const result = await fetch("/api", {
        body: new FormData(formEl),
        method: "post",
      })
      const blob = await result.blob()
      const objectURL = URL.createObjectURL(blob);
      locationImgEl.src = objectURL;
    })

    canvasEl.addEventListener('mousedown', (e) => {
      if (e.button == 0) {
        mousedDown = true
      } else {
        mousedDown = false
      }
    })

    canvasEl.addEventListener('mouseup', () => {
      mousedDown = false
    })

    canvasEl.addEventListener('mousemove', (e) => {
      if (mousedDown) {
        const x =  e.layerX - (bernieImageWidth / 2)
        const y =  e.layerY - (bernieImageHeight / 2)
        draw(x, y)
      }
    })

    locationImgEl.addEventListener('load', () => {
      downloadButtonEl.hidden = '';
      draw()
    })

    bernieImageEl.addEventListener('load', () => {
      bernieImageWidth = bernieImageEl.width;
      bernieImageHeight = bernieImageEl.height;
    })

    downloadButtonEl.addEventListener('click', downloadBernie)
})
