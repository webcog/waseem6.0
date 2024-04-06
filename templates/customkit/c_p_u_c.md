{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
<!-- Meta -->
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="">
<meta name="author" content="">
<meta name="keywords" content="MediaCenter, Template, eCommerce">
<meta name="robots" content="all">
<title>{% block title %}{% endblock title %} - Tie</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/fabric.js/5.3.1/fabric.min.js" integrity="sha512-CeIsOAsgJnmevfCi2C7Zsyy6bQKi43utIjdA87Q0ZY84oDqnI0uwfM9+bKiIkI75lUeI00WG/+uJzOmuHlesMA==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<!-- Bootstrap Core CSS -->
<link rel="stylesheet" href="{% static 'assets/css/bootstrap.min.css' %}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Boogaloo&family=Lalezar&family=Madimi+One&family=Montserrat:ital,wght@0,100..900;1,100..900&family=Oswald:wght@200..700&family=Pacifico&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Sora:wght@100..800&display=swap" rel="stylesheet">

<!-- Customizable CSS -->
<link rel="stylesheet" href="{% static 'assets/css/main.css' %}">
<link rel="stylesheet" href="{% static 'assets/css/blue.css' %}">
<link rel="stylesheet" href="{% static 'assets/css/owl.carousel.css' %}">
<link rel="stylesheet" href="{% static 'assets/css/owl.transitions.css' %}">
<link rel="stylesheet" href="{% static 'assets/css/animate.min.css' %}">
<link rel="stylesheet" href="{% static 'assets/css/rateit.css' %}">
<link rel="stylesheet" href="{% static 'assets/css/bootstrap-select.min.css' %}">
<link href="{% static 'assets/css/lightbox.css' %}" rel="stylesheet">

<!-- Icons/Glyphs -->
<link rel="stylesheet" href="{% static 'assets/css/font-awesome.css' %}">

<!-- Fonts -->
<link href="https://fonts.googleapis.com/css?family=Barlow:200,300,300i,400,400i,500,500i,600,700,800" rel="stylesheet">
<link href='http://fonts.googleapis.com/css?family=Roboto:300,400,500,700' rel='stylesheet' type='text/css'>
<link href='https://fonts.googleapis.com/css?family=Open+Sans:400,300,400italic,600,600italic,700,700italic,800' rel='stylesheet' type='text/css'>
<link href='https://fonts.googleapis.com/css?family=Montserrat:400,700' rel='stylesheet' type='text/css'>
</head>
<body class="cnt-home">



{% include "includes/navbar.html" %}


<button type="button" id="toggle-menu-2" style="position: fixed;right: 0;z-index: 1000;padding: 10px;background: #fff;border: 1px solid black;width: 40px;"><i class="fa fa-bars"></i></button>


    <div class="body-content outer-top-xs">
        <div class='container'>
            <div class='row single-product'>
                <div class='col-xs-12 col-sm-12 col-md-3 sidebar'>
                    <div class="sidebar-module-container">
                   	
      
        
                        <div class="row g-0 hidden-xs">
                            {% for gallery_image in product_gallery %}

                            <div class="col-md-6 col-sm-6 col-6" style="margin-top: 10px;">

                                <img class="img-responsive" style="height: 115px;width: 115px;border: 1px solid black;" src="{{gallery_image.image.url}}" alt="">
                            </div>
                            {% endfor %}

                            
                        </div>
        
    <!-- ============================================== Testimonials: END ============================================== -->
    
    
    
                    </div>
                </div><!-- /.sidebar -->
          
                <div class='col-xs-12 col-sm-12 col-md-9 rht-col'>
                <div class="detail-block">
                    <div class="row"> 
                        <style>
                        canvas {
                            border: 1px solid #ccc;
                        }
                        #controls {
                            /* margin-top: 10px; */
                        }
                        .btn-cstm {
                        background-color: transparent;
                        padding: 5px;
                        outline: none;
                        border: none;
                        font-size: 18px;
                        border-bottom: none;
                        transition: background-color 0.3s, box-shadow 0.3s;
                    }

                    
                    .btn-cstm:hover {
                        background-color: #157ed2; 
                        color: #fff;
                    }
                    </style>
                    
                        <div class="col-xs-12 col-sm-12 col-md-4 col-lg-4 gallery-holder">
                            <div class="product-item-holder size-big single-product-gallery small-gallery">
                                <button title="Rotate" class="btn-cstm" type="button" onclick="rotate()"><i class="fa fa-refresh"></i></button>
                                <button title="Delete" class="btn-cstm" type="button" onclick="deleteObject()"><i class="fa fa-trash"></i></button>
                                <button title="Zoom In" class="btn-cstm" type="button" onclick="resizePlus()"><i class="fa fa-search-plus"></i></button>
                                <button title="Zoom Out" class="btn-cstm" type="button" onclick="resizeMinus()"><i class="fa fa-search-minus"></i></button>
                                <button title="Undo" class="btn-cstm" type="button" onclick="undo()"><i class="fa fa-undo"></i></button>
                                <button title="Redo" class="btn-cstm" type="button" onclick="redo()"><i class="fa fa-repeat"></i></button>
                                <button title="Show Grid" id="toggleBtn" class="btn-cstm" type="button" onclick="toggleGrid()"><i id="gridIcon" class="fa fa-th"></i></button>

                                
                                <!-- <input type=""> -->
                                <!-- <input type="range" id="gridSpacing" min="10" max="100" value="20" onchange="changeGridSpacing()"> -->
                                <!-- <hr> -->
                                <!-- Main product image -->
                                <div id="owl-single-product">
                                    
                                    <div class="single-product-gallery-item" id="slide1">
                                        
                                        
                                        <canvas class="img-responsive main-product-image" id="canvas" width="280" height="400"></canvas>
  
                                        <!-- <img class="img-responsive main-product-image" alt="" src="{{ single_product.images.url }}" /> -->

                                    </div>
                                </div>
<style>
   
input[type=range]::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background-color: #000;
  cursor: pointer;
}
</style>
                                                                                                                      <input style="-webkit-appearance: none;background-color: #ccc;border-radius: 0px;outline: none;color: black;" type="range" id="gridSpacing" min="10" max="100" value="20" onchange="changeGridSpacing()">



                                                                                                                      
                        
                               
                        
                            </div>
                        </div>
                        	<form  action="{% url 'custom_add_to_cart' single_product.id %}" method="POST">
                                {% csrf_token %}
                        <div class='col-sm-12 col-md-8 col-lg-8 product-info-block'>
                            <div class="product-info">
                                <h1 class="name">{{single_product.product_name}} | 280x400</h1>
                                
                                <div class="rating-reviews m-t-20">
                                    <div class="row">
                                    <div class="col-lg-12">
                                        <div class="pull-left">
                                            <div class="">
                                                <i class="fa fa-star{% if single_product.average_review < 0.5 %}-o{% elif single_product.average_review >= 0.5 and single_product.average_review < 1%}-half-o{% endif %}"
                                                    aria-hidden="true"></i>
                                                <i class="fa fa-star{% if single_product.average_review < 1.5 %}-o{% elif single_product.average_review >= 1.5 and single_product.average_review < 2%}-half-o{% endif %}"
                                                    aria-hidden="true"></i>
                                                <i class="fa fa-star{% if single_product.average_review < 2.5 %}-o{% elif single_product.average_review >= 2.5 and single_product.average_review < 3%}-half-o{% endif %}"
                                                    aria-hidden="true"></i>
                                                <i class="fa fa-star{% if single_product.average_review < 3.5 %}-o{% elif single_product.average_review >= 3.5 and single_product.average_review < 4%}-half-o{% endif %}"
                                                    aria-hidden="true"></i>
                                                <i class="fa fa-star{% if single_product.average_review < 4.5 %}-o{% elif single_product.average_review >= 4.5 and single_product.average_review < 5%}-half-o{% endif %}"
                                                    aria-hidden="true"></i>
                                            </div>
                                        </div>
                                        <div class="pull-left">
                                            <div class="reviews">
                                                <a href="#" class="lnk">({{ single_product.count_review }}  Reviews)</a>
                                            </div>
                                        </div>
                                        </div>
                                    </div><!-- /.row -->		
                                </div><!-- /.rating-reviews -->

                                <div class="" style="margin-top: 10px;">

                                    
                                    <input type="radio" checked>
                                    <label for="">Create Your Own</label>
                                </div>

                                <h5> -Type Text</h5>
                                <p><b>Note! You Can Add Multiple Text Here!</b></p>
                               <div class="row">
                                <div class="col-md-8">

                                    <input class="form-control" type="text" id="textInput" placeholder="Type Text..." style="padding: 5px;border-radius: 0;border: 1px solid black;">
                                </div>

                                <div class="col-md-4">
                                    <style>
                                        .btn-add-txt{
                                            border-radius: 0;
                                            padding: 6px;
                                            border: 1px solid black;
                                        }
                                        .btn-add-txt:hover{
                                            background-color: #e9e5e5;
                                        }
                                        .btn-add-txt:active{
                                            background: #dfdddd;

                                        }
                                        .btn-add-txt:focus, .btn-add-txt:active{
                                            outline: none !important;
                                            box-shadow: none !important;
                                            /* border: none !important; */
                                        }
                                    </style>
                                    <button class="btn btn-add-txt" type="button" onclick="addText()">Add Text</button>
                                </div>
                               </div>

                               


                               
                               
                               
                               
                                <br>
                                <div class="row">
                                    <div class="col-md-8">
                                        <select class="form-control" style="padding: 5px;border-radius: 0;border: 1px solid black;" id="fontSelect" onchange="changeFont()">
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
                                    </div>
                                    <div class="col-md-4">
                                        <input  class="btn-add-txt" style="width: 68px;height: 33px;" type="color" id="colorPicker" onchange="changeColor()" value="#000000">

                                    </div>
                                </div>
                                
                           
                                <div id="controls">
                                    <style>
                                        .cstm-img{
                                            padding: 8px;background-color:transparent;cursor: pointer;border: 1px solid #ccc;
                                            width: 100%;
                                            text-align: center;
                                        }
                                        .cstm-img:hover{
                                            background-color: #ccc;
                                            
                                        }
                                    </style>
                                    <h5> -Add Image</h5>
                                    <p><b>Note! You Can Add Multiple Images Here!</b></p>
                                    <label class="cstm-img" for="imageLoader" >Upload Image</label>
                                    <input class="" type="file" id="imageLoader" style="display: none;">

                                    <button type="button" id="toggle-menu-1" class="cstm-img">Use Default Logos</button>
                                  </div>



    
                                <div class="stock-container info-container m-t-10">
                                    <div class="row">
                                    <div class="col-lg-12">
                                        <div class="pull-left">
                                            <div class="stock-box">
                                                <span class="label">Availability :</span>
                                            </div>	
                                        </div>
                                        <div class="pull-left">
                                            <div class="stock-box">
                                                {% if single_product.stock <= 0 %} 
                                                <span class="value">Out Of Stock</span>
                                                {% else %}
                                                <span class="value">In Stock</span>
                                                {% endif %}
                                            </div>	
                                        </div>
                                        </div>
                                    </div><!-- /.row -->	
                                </div><!-- /.stock-container -->
    
                                <div class="description-container m-t-20">
                                    <p>
                                        {{single_product.description|truncatewords:15}}
                                    </p>
                                </div><!-- /.description-container -->
    
                                <div class="price-container info-container m-t-30">
                                    <div class="row">
                                        
    
                                        <div class="col-sm-6 col-xs-6">
                                            <div class="price-box">
                                                {% if single_product.stock <= 0 %} 
                                                
                                                <span class="price">Out of Stock</span>
                                                {% else %}
                                                <span class="price">PKR {{single_product.price}}</span>
                                                <span class="price-strike">$900.00</span>
                                                {% endif %}
                                            </div>
                                        </div>
    
                                     
    
                                    </div><!-- /.row -->
                                </div><!-- /.price-container -->

                             
                                {% if single_product.stock <= 0 %} 
                                {% else %}
                                <div class="quantity-container info-container">
                                    <div class="">

                                       
                                       

                                        {% if single_product.variation_set.colors %}

                                        <div class="qty">
                                            <span class="label">Color :</span>
                                        </div>
                                        <style>
                                            .qty-count input[type="color"] {
                                                border-radius: 0 !important;
                                                border: none !important;
                                                outline: none !important;
                                                box-shadow: none !important;
                                            }
                                        </style>
                                        <div class="qty-count">
                                            <div class="cart-quantity">
                                                <div class="quant-input">
                                                    <!-- {% for i in single_product.variation_set.colors %}
                                                    <input type="color" class="form-control border-0">
                                                    {% endfor %} -->
                                                    {% for i in single_product.variation_set.sizes %}
                                                         <input type="color" class="form-control border-0" value="{{ i.variation_value }}">
                                                    {% endfor %}
                                                    
                                                    <!-- <select name="color" class="form-control" required>
                                                        <option value="" disabled selected>Select</option>
                                                        {% for i in single_product.variation_set.colors %}
                                                        <option value="{{ i.variation_value | lower }}">
                                                            {{ i.variation_value | capfirst }}
                                                        </option>
                                                        {% endfor %}
                                                    </select> -->
                                              </div>
                                            </div>
                                        </div>
                                        
                                        {% endif %}
                                        {% if single_product.variation_set.sizes %}

                                        <div class="qty">
                                            <span class="label">Size :</span>
                                        </div>
                                        
                                        <div class="qty-count">
                                            <div class="cart-quantity">
                                                <div class="quant-input">
                                                    <select name="size" class="form-control" required>
                                                        <option value="" disabled selected>Select</option>
                                                        {% for i in single_product.variation_set.sizes %}
                                                        <option value="{{ i.variation_value | lower }}">
                                                            {{ i.variation_value | capfirst }}
                                                        </option>
                                                        {% endfor %}
                                                    </select>
                                              </div>
                                            </div>
                                        </div>
                                        
                                        {% endif %}

                                        <div class="qty" style="visibility: hidden;">
                                            <span class="label">Color :</span>
                                        </div>
                                        
                                        <div class="qty-count" style="visibility: hidden;">
                                            <div class="cart-quantity">
                                                <div class="quant-input">
                                                    <input type="color" class="form-control border-0">
                                                   {% comment %} <select class="form-control" name="" id="">
                                                    <option value="">red</option>
                                                   </select> {% endcomment %}
                                              </div>
                                            </div>
                                        </div>
    
                                        <div class="add-btn" style="margin-top: 15px;">
                                            <button type="submit"  class="btn btn-primary"><i class="fa fa-shopping-cart inner-right-vs"></i> ADD TO CART</button>
                                        </div>

                                        <!-- Button trigger modal -->

                                        
                                    </div><!-- /.row -->
                                </div><!-- /.quantity-container -->
                                {% endif %}

                                
    
                                
    
                                
                            </div><!-- /.product-info -->
                        </div>
                        </form>
                    <!-- /.col-sm-7 -->
                    </div><!-- /.row -->
                    </div>
                    
                    <div class="product-tabs inner-bottom-xs">
                        <div class="row">
                            <div class="col-sm-12 col-md-3 col-lg-3">
                                <ul id="product-tabs" class="nav nav-tabs nav-tab-cell">
                                    <li class="active"><a data-toggle="tab" href="#description">DESCRIPTION</a></li>
                                    <li><a data-toggle="tab" href="#review">REVIEW</a></li>
                                </ul><!-- /.nav-tabs #product-tabs -->
                            </div>
                            <div class="col-sm-12 col-md-9 col-lg-9">
    
                                <div class="tab-content">
                                    
                                    <div id="description" class="tab-pane in active">
                                        <div class="product-tab">
                                            <p class="text">
                                                {{single_product.description}}
                                            </p>
                                        </div>	
                                    </div><!-- /.tab-pane -->
    
                                    <div id="review" class="tab-pane">
                                        <div class="product-tab">
                                                                                    
                                            <div class="product-reviews">
                                                <h4 class="title">Customer Reviews</h4>
    
                                                <div class="reviews">
                                                    <div class="review">
                                                        <div class="review-title"><span class="summary">We love this product</span><span class="date"><i class="fa fa-calendar"></i><span>1 days ago</span></span></div>
                                                        <div class="text">"Lorem ipsum dolor sit amet, consectetur adipiscing elit.Aliquam suscipit."</div>
                                                                                                            </div>
                                                
                                                </div><!-- /.reviews -->
                                            </div><!-- /.product-reviews -->
                                            
    
                                            
                                            <div class="product-add-review">
                                                <h4 class="title">Write your own review</h4>
                                                <div class="review-table">
                                                    <div class="table-responsive">
                                                        <table class="table">	
                                                            <thead>
                                                                <tr>
                                                                    <th class="cell-label">&nbsp;</th>
                                                                    <th>1 star</th>
                                                                    <th>2 stars</th>
                                                                    <th>3 stars</th>
                                                                    <th>4 stars</th>
                                                                    <th>5 stars</th>
                                                                </tr>
                                                            </thead>	
                                                            <tbody>
                                                                <tr>
                                                                    <td class="cell-label">Quality</td>
                                                                    <td><input type="radio" name="quality" class="radio" value="1"></td>
                                                                    <td><input type="radio" name="quality" class="radio" value="2"></td>
                                                                    <td><input type="radio" name="quality" class="radio" value="3"></td>
                                                                    <td><input type="radio" name="quality" class="radio" value="4"></td>
                                                                    <td><input type="radio" name="quality" class="radio" value="5"></td>
                                                                </tr>
                                                                <tr>
                                                                    <td class="cell-label">Price</td>
                                                                    <td><input type="radio" name="quality" class="radio" value="1"></td>
                                                                    <td><input type="radio" name="quality" class="radio" value="2"></td>
                                                                    <td><input type="radio" name="quality" class="radio" value="3"></td>
                                                                    <td><input type="radio" name="quality" class="radio" value="4"></td>
                                                                    <td><input type="radio" name="quality" class="radio" value="5"></td>
                                                                </tr>
                                                                <tr>
                                                                    <td class="cell-label">Value</td>
                                                                    <td><input type="radio" name="quality" class="radio" value="1"></td>
                                                                    <td><input type="radio" name="quality" class="radio" value="2"></td>
                                                                    <td><input type="radio" name="quality" class="radio" value="3"></td>
                                                                    <td><input type="radio" name="quality" class="radio" value="4"></td>
                                                                    <td><input type="radio" name="quality" class="radio" value="5"></td>
                                                                </tr>
                                                            </tbody>
                                                        </table><!-- /.table .table-bordered -->
                                                    </div><!-- /.table-responsive -->
                                                </div><!-- /.review-table -->
                                                
                                                <div class="review-form">
                                                    <div class="form-container">
                                                        <form class="cnt-form">
                                                            
                                                            <div class="row">
                                                                <div class="col-sm-6">
                                                                    <div class="form-group">
                                                                        <label for="exampleInputName">Your Name <span class="astk">*</span></label>
                                                                        <input type="text" class="form-control txt" id="exampleInputName" placeholder="">
                                                                    </div><!-- /.form-group -->
                                                                    <div class="form-group">
                                                                        <label for="exampleInputSummary">Summary <span class="astk">*</span></label>
                                                                        <input type="text" class="form-control txt" id="exampleInputSummary" placeholder="">
                                                                    </div><!-- /.form-group -->
                                                                </div>
    
                                                                <div class="col-md-6">
                                                                    <div class="form-group">
                                                                        <label for="exampleInputReview">Review <span class="astk">*</span></label>
                                                                        <textarea class="form-control txt txt-review" id="exampleInputReview" rows="4" placeholder=""></textarea>
                                                                    </div><!-- /.form-group -->
                                                                </div>
                                                            </div><!-- /.row -->
                                                            
                                                            <div class="action text-right">
                                                                <button class="btn btn-primary btn-upper">SUBMIT REVIEW</button>
                                                            </div><!-- /.action -->
    
                                                        </form><!-- /.cnt-form -->
                                                    </div><!-- /.form-container -->
                                                </div><!-- /.review-form -->
    
                                            </div><!-- /.product-add-review -->										
                                            
                                        </div><!-- /.product-tab -->
                                    </div><!-- /.tab-pane -->
    
                                   
                                </div><!-- /.tab-content -->
                            </div><!-- /.col -->
                        </div><!-- /.row -->
                    </div><!-- /.product-tabs -->
    
      

<style>
 

 .offcanvas {
    position: fixed;
    top: 0;
    right: -350px; /* Start off-canvas on the right side */
    width: 275px; /* Width of off-canvas menu */
    height: 100%;
    background-color: #fff;
    z-index: 1050;
    transition: right 0.5s ease; /* Animation for transition */
}

.offcanvas-content {
    padding: 20px;
    overflow-y: auto; /* Enable vertical scrolling */
    max-height: calc(100% - 80px); /* Set maximum height for content */
}
.offcanvas-content::-webkit-scrollbar {
    width: 4px; /* Width of the scrollbar */
}

.offcanvas-content::-webkit-scrollbar-track {
    background: transparent; /* Track color */
}

.offcanvas-content::-webkit-scrollbar-thumb {
    background: #000; /* Thumb color */
    border-radius: 0; /* Border radius */
}

.offcanvas-content::-webkit-scrollbar-thumb:hover {
    background: #555; /* Thumb color on hover */
}

.close-btn {
    position: absolute;
    top: 10px;
    right: 10px;
    font-size: 34px;
    cursor: pointer;
    background: transparent;
    border: none;
    z-index: 10000;
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




<div id="offcanvas-menu" class="offcanvas">
    <button id="close-menu" class="close-btn">&times;</button>
    <div class="offcanvas-content">
        <!-- Your off-canvas content goes here -->
        <div class="row">
            {% for logo in custom_logo %}
            <div class="col-md-6">
                <img src="{{logo.image.url}}" style="height: 115px;width: 115px;border-bottom: 1px solid black;"  class="img-responsive" alt="">
            </div>
            {% endfor %}
           
            
            
        </div>
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
        offcanvasMenu.style.right = '-350px'; // Slide out the off-canvas menu
        overlay.style.display = 'none';
    });

    overlay.addEventListener('click', function() {
        offcanvasMenu.style.right = '-350px'; // Slide out the off-canvas menu
        overlay.style.display = 'none';
    });

    function toggleOffcanvasMenu() {
        var currentState = offcanvasMenu.style.right;
        if (currentState === '0px' || currentState === '') {
            offcanvasMenu.style.right = '-350px'; // Slide out the off-canvas menu
            overlay.style.display = 'none';
        } else {
            offcanvasMenu.style.right = '0'; // Slide in the off-canvas menu
            overlay.style.display = 'block';
        }
    }
});


</script>
    <!-- ============================================== UPSELL PRODUCTS : END ============================================== -->
                
                </div><!-- /.col -->
                <div class="clearfix"></div>
            </div><!-- /.row -->
            <!-- ============================================== BRANDS CAROUSEL ============================================== -->
    
    <!-- ============================================== BRANDS CAROUSEL : END ============================================== -->	</div><!-- /.container -->
    </div><!-- /.body-content -->
    
    <!-- ============================================================= FOOTER ============================================================= -->
    
            <!-- ============================================== INFO BOXES ============================================== -->
            
            <!-- /.info-boxes --> 
            <!-- ============================================== INFO BOXES : END ============================================== --> 
    
    <!-- ============================================================= FOOTER ============================================================= -->
  {% include "includes/footer.html" %}



<script src="{% static 'assets/js/jquery-1.11.1.min.js' %}"></script>
<script src="{% static 'assets/js/bootstrap.min.js' %}"></script>
<script src="{% static 'assets/js/bootstrap-hover-dropdown.min.js' %}"></script>
<script src="{% static 'assets/js/owl.carousel.min.js' %}"></script>
<script src="{% static 'assets/js/echo.min.js' %}"></script>
<script src="{% static 'assets/js/jquery.easing-1.3.min.js' %}"></script>
<script src="{% static 'assets/js/bootstrap-slider.min.js' %}"></script>
<script src="{% static 'assets/js/jquery.rateit.min.js' %}"></script>
<script src="{% static 'assets/js/lightbox.min.js' %}"></script>
<script src="{% static 'assets/js/bootstrap-select.min.js' %}"></script>
<script src="{% static 'assets/js/wow.min.js' %}"></script>
<script src="{% static 'assets/js/scripts.js' %}"></script>








<script>
    var canvas = new fabric.Canvas('canvas');
    var backgroundImageUrl = `{{single_product.images.url}}`; 
    var backgroundImage; 
    var selectedFont = 'Arial'; 
    var activeTextObject;
    var undoStack = [];
    var redoStack = [];
    var gridSpacing = 20;
    // var showGrid = true;

    // Function to add default background image
    function addDefaultBackgroundImage() {
        fabric.Image.fromURL(backgroundImageUrl, function(img) {
            img.scaleToWidth(canvas.width);
            img.scaleToHeight(canvas.height);
            canvas.setBackgroundImage(img, canvas.renderAll.bind(canvas));
            backgroundImage = img;
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
    // function toggleGrid() {
    //     showGrid = !showGrid;
    //     canvas.renderAll();
    // }
    var showGrid = false;

    function toggleGrid() {
    showGrid = !showGrid;
    if (showGrid) {
        document.getElementById("gridIcon").classList.remove("fa-th");
        document.getElementById("gridIcon").classList.add("fa-th-large");
    } else {
        document.getElementById("gridIcon").classList.remove("fa-th-large");
        document.getElementById("gridIcon").classList.add("fa-th");
    }
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

    // Initialize canvas with default background image
    addDefaultBackgroundImage();
</script>



</body>

</html>