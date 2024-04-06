<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Editor</title>
    <style>
        canvas {
            border: 1px solid #ccc;
        }
        #controls {
            margin-top: 10px;
        }
        .image-gallery img {
            width: 100px;
            height: auto;
            margin: 5px;
            cursor: pointer;
        }
        .overlay-gallery img {
            width: 100px;
            height: auto;
            margin: 5px;
            cursor: pointer;
            opacity: 0.5;
        }
        .overlay-gallery img:hover {
            opacity: 1;
        }
    </style>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Boogaloo&family=Lalezar&family=Madimi+One&family=Montserrat:ital,wght@0,100..900;1,100..900&family=Oswald:wght@200..700&family=Pacifico&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Sora:wght@100..800&display=swap" rel="stylesheet">
    <script src="fabric.min.js"></script>
</head>
<body>
    <canvas id="canvas" width="280" height="400"></canvas>
    <div class="image-gallery">
        <img src="d.jpg" onclick="replaceBackgroundImage(this.src)">
        <img src="shirt.png" onclick="replaceBackgroundImage(this.src)">
        <!-- Add more images as needed -->
    </div>
    <div class="overlay-gallery">
        <img src="d.jpg" onclick="addOverlayImage(this.src)">
        <img src="shirt.png" onclick="addOverlayImage(this.src)">
        <!-- Add more images as needed -->
    </div>
    <div id="controls">
        <label>Add Image: <input type="file" id="imageLoader"></label>
        <button onclick="rotate()">Rotate</button>
        <button onclick="resizePlus()">Resize +</button>
        <button onclick="resizeMinus()">Resize -</button>
        <button onclick="deleteObject()">Delete</button>
        <button onclick="undo()">Undo</button>
        <button onclick="redo()">Redo</button>
        <button onclick="toggleGrid()">Toggle Grid</button>
        <!-- <input type=""> -->
        <input type="range" id="gridSpacing" min="10" max="100" value="20" onchange="changeGridSpacing()">
        <label for="gridSpacing">Grid Spacing</label>
        <select id="fontSelect" onchange="changeFont()">
            <option style="font-family:Arial ;" value="Arial">Arial</option>
            <option style="font-family:Boogaloo ;" value="Boogaloo">Boogaloo</option>
            <option style="font-family:Lalezar ;" value="Lalezar">Lalezar</option>
            <option style="font-family:'Madimi One' ;" value="Madimi One">Madimi One</option>
            <option style="font-family: Montserrat;" value="Montserrat">Montserrat</option>
            <option style="font-family: Oswald;" value="Oswald">Oswald</option>
            <option style="font-family: Pacifico;" value="Pacifico">Pacifico</option>
            <option style="font-family: Poppins;" value="Poppins">Poppins</option>
            <option style="font-family: Sora;" value="Sora">Sora</option>
        </select>
        <input type="color" id="colorPicker" onchange="changeColor()" value="#000000">
    </div>

    <input type="text" id="textInput" style="margin-top: 10px;">
    <button onclick="addText()">Add Text</button>

    <script>
        var canvas = new fabric.Canvas('canvas');
        var selectedFont = 'Arial'; 
        var activeTextObject;
        var undoStack = [];
        var redoStack = [];
        var gridSpacing = 20;
        var showGrid = true;


        function replaceBackgroundImage(imageUrl) {
            fabric.Image.fromURL(imageUrl, function(img) {
                img.scaleToWidth(canvas.width);
                img.scaleToHeight(canvas.height);
                canvas.setBackgroundImage(img, canvas.renderAll.bind(canvas));
            });
        }

        // Function to add default background image
        function addDefaultBackgroundImage() {
            var backgroundImageUrl = 'shirtTwo.png'; // Replace 'defaultImage.jpg' with the path to your default image
            fabric.Image.fromURL(backgroundImageUrl, function(img) {
                img.scaleToWidth(canvas.width);
                img.scaleToHeight(canvas.height);
                canvas.setBackgroundImage(img, canvas.renderAll.bind(canvas));
            });
        }


        // Function to add text to canvas
        function addText() {
            var text = document.getElementById("textInput").value;
            if (text !== "") {
                if (activeTextObject) {
                    // Update existing text
                    activeTextObject.set('text', text);
                    activeTextObject.set('fill', document.getElementById("colorPicker").value);
                    activeTextObject.set('fontFamily', selectedFont);
                    canvas.renderAll();
                } else {
                    // Add new text
                    var textObject = new fabric.Text(text, {
                        left: 100,
                        top: 100,
                        fill: document.getElementById("colorPicker").value, // Set text color
                        fontSize: 20,
                        fontFamily: selectedFont // Set font family
                    });
                    canvas.add(textObject);
                    canvas.setActiveObject(textObject);
                }
                addToUndoStack();
            }
        }

        // Function to delete selected object
        function deleteObject() {
            var activeObject = canvas.getActiveObject();
            if (activeObject) {
                canvas.remove(activeObject);
                addToUndoStack();
            }
        }

        // Function to rotate selected object
        function rotate() {
            var activeObject = canvas.getActiveObject();
            if (activeObject) {
                activeObject.rotate(activeObject.angle + 45);
                canvas.renderAll();
                addToUndoStack();
            }
        }

        // Function to resize selected object by scaling
        function resizePlus() {
            var activeObject = canvas.getActiveObject();
            if (activeObject) {
                activeObject.scaleX *= 1.1;
                activeObject.scaleY *= 1.1;
                canvas.renderAll();
                addToUndoStack();
            }
        }

        function resizeMinus() {
            var activeObject = canvas.getActiveObject();
            if (activeObject) {
                activeObject.scaleX *= 0.9;
                activeObject.scaleY *= 0.9;
                canvas.renderAll();
                addToUndoStack();
            }
        }

        // Function to change font family
        function changeFont() {
            selectedFont = document.getElementById("fontSelect").value;
            var activeObject = canvas.getActiveObject();
            if (activeObject && activeObject.type === 'text') {
                activeObject.set('fontFamily', selectedFont);
                canvas.renderAll();
                addToUndoStack();
            }
        }

        // Function to change text color
        function changeColor() {
            var activeObject = canvas.getActiveObject();
            if (activeObject && activeObject.type === 'text') {
                activeObject.set('fill', document.getElementById("colorPicker").value);
                canvas.renderAll();
                addToUndoStack();
            }
        }

        // Function to toggle grid visibility
        function toggleGrid() {
            showGrid = !showGrid;
            canvas.renderAll();
        }

        // Function to change grid spacing
        function changeGridSpacing() {
            gridSpacing = parseInt(document.getElementById("gridSpacing").value);
            canvas.renderAll();
        }

        // Function to add action to undo stack
        function addToUndoStack() {
            undoStack.push(canvas.toDatalessJSON());
            redoStack = []; // Clear redo stack when new action is performed
        }

        // Function to undo
        function undo() {
            if (undoStack.length > 1) {
                redoStack.push(undoStack.pop());
                var jsonData = undoStack[undoStack.length - 1];
                canvas.loadFromJSON(jsonData, canvas.renderAll.bind(canvas));
            }
        }

        // Function to redo
        function redo() {
            if (redoStack.length > 0) {
                var jsonData = redoStack.pop();
                undoStack.push(jsonData);
                canvas.loadFromJSON(jsonData, canvas.renderAll.bind(canvas));
            }
        }

        // Function to snap to grid
        function snapToGrid(value) {
            return Math.round(value / gridSpacing) * gridSpacing;
        }

        // Event listener to render grid
        canvas.on('after:render', function() {
            if (showGrid) {
                var ctx = canvas.getContext('2d');
                ctx.save();
                ctx.strokeStyle = '#ccc';
                ctx.lineWidth = 1;
                for (var x = 0; x < canvas.width; x += gridSpacing) {
                    for (var y = 0; y < canvas.height; y += gridSpacing) {
                        ctx.beginPath();
                        ctx.moveTo(x, y);
                        ctx.lineTo(x, canvas.height);
                        ctx.stroke();
                        ctx.beginPath();
                        ctx.moveTo(x, y);
                        ctx.lineTo(canvas.width, y);
                        ctx.stroke();
                    }
                }
                ctx.restore();
            }
        });

        // Event listener to snap objects to grid
        canvas.on('object:moving', function(e) {
            if (showGrid) {
                var obj = e.target;
                obj.set({
                    left: snapToGrid(obj.left),
                    top: snapToGrid(obj.top)
                });
            }
        });

        // Image loader
        var imageLoader = document.getElementById('imageLoader');
        imageLoader.addEventListener('change', function(e) {
            var file = e.target.files[0];
            var reader = new FileReader();
            reader.onload = function() {
                addImage(reader.result);
            }
            reader.readAsDataURL(file);
        });

        // Function to add image to canvas
        function addImage(url) {
            fabric.Image.fromURL(url, function(img) {
                // Set properties like scaling, rotating, dragging
                img.scale(0.5).set({
                    left: 100,
                    top: 100,
                    transparentCorners: false,
                    cornerColor: 'blue',
                    cornerSize: 10,
                    opacity: 0.8 // Set opacity to 0.5 for new images
                });
                canvas.add(img);
                canvas.setActiveObject(img);
                addToUndoStack();
            });
        }

        // Event listener to set active text object
        canvas.on('object:selected', function(e) {
            if (e.target.type === 'text') {
                activeTextObject = e.target;
                document.getElementById("textInput").value = activeTextObject.text;
                document.getElementById("colorPicker").value = activeTextObject.fill;
                document.getElementById("fontSelect").value = activeTextObject.fontFamily;
            }
        });

        // Event listener to clear active text object when deselected
        canvas.on('selection:cleared', function() {
            activeTextObject = null;
            document.getElementById("textInput").value = "";
            document.getElementById("colorPicker").value = "#000000";
            document.getElementById("fontSelect").value = "Arial";
        });


        function addOverlayImage(imageUrl) {
            fabric.Image.fromURL(imageUrl, function(img) {
                img.set({
                    left: 0,
                    top: 0,
                    scaleX: canvas.width / img.width,
                    scaleY: canvas.height / img.height,
                    selectable: true,
                    opacity: 0.8 // Set overlay image opacity
                });
                canvas.add(img);
                addToUndoStack();
            });
        }

        // Initialize canvas with default background image
        addDefaultBackgroundImage();

    </script>
</body>
</html>
