<button id="toggle-menu-2" class="btn btn-default">Toggle Menu 2</button>

<div id="offcanvas-menu" class="offcanvas">
    <button id="close-menu" class="close-btn">&times;</button>
    <div class="offcanvas-content">
        <!-- Your off-canvas content goes here -->
        <ul>
            <li><a href="#">Link 1</a></li>
            <li><a href="#">Link 2</a></li>
            <li><a href="#">Link 3</a></li>
        </ul>
    </div>
</div>

<div id="overlay" class="overlay"></div>







<script>


    document.addEventListener('DOMContentLoaded', function() {
        var toggleMenu1Btn = document.getElementById('toggle-menu-1');
        var toggleMenu2Btn = document.getElementById('toggle-menu-2');
        var closeMenuBtn = document.getElementById('close-menu');
        var offcanvasMenu = document.getElementById('offcanvas-menu');
        var overlay = document.getElementById('overlay');
    
        toggleMenu1Btn.addEventListener('click', function() {
            toggleOffcanvasMenu();
        });
    
        toggleMenu2Btn.addEventListener('click', function() {
            toggleOffcanvasMenu();
        });
    
        closeMenuBtn.addEventListener('click', function() {
            offcanvasMenu.style.right = '-300px'; // Slide out the off-canvas menu
            overlay.style.display = 'none';
        });
    
        overlay.addEventListener('click', function() {
            offcanvasMenu.style.right = '-300px'; // Slide out the off-canvas menu
            overlay.style.display = 'none';
        });
    
        function toggleOffcanvasMenu() {
            var currentState = offcanvasMenu.style.right;
            if (currentState === '0px' || currentState === '') {
                offcanvasMenu.style.right = '-300px'; // Slide out the off-canvas menu
                overlay.style.display = 'none';
            } else {
                offcanvasMenu.style.right = '0'; // Slide in the off-canvas menu
                overlay.style.display = 'block';
            }
        }
    });
    
    
    </script>



    <style>
 

        .offcanvas {
           position: fixed;
           top: 0;
           right: -300px; /* Start off-canvas on the right side */
           width: 250px; /* Width of off-canvas menu */
           height: 100%;
           background-color: #fff;
           z-index: 1050;
           transition: right 0.5s ease; /* Animation for transition */
       }
       
       .offcanvas-content {
           padding: 20px;
       }
       
       .close-btn {
           position: absolute;
           top: 10px;
           right: 10px;
           font-size: 24px;
           cursor: pointer;
       }
       
       .overlay {
           position: fixed;
           top: 0;
           left: 0;
           width: 100%;
           height: 100%;
           background-color: rgba(0, 0, 0, 0.5);
           z-index: 1040;
           display: none;
       }
       
       
       
       </style>
       