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

<!-- Bootstrap Core CSS -->
<link rel="stylesheet" href="{% static 'assets/css/bootstrap.min.css' %}">

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

    <div class="body-content outer-top-xs">
        <div class='container'>
            <div class='row single-product'>
                <div class='col-xs-12 col-sm-12 col-md-3 sidebar'>
                    <div class="sidebar-module-container">
                   	
      
        
        
            <!-- ============================================== HOT DEALS ============================================== -->
    <div class="sidebar-widget hot-deals outer-bottom-xs">
              <h3 class="section-title">Hot deals</h3>
              <div class="owl-carousel sidebar-carousel custom-carousel owl-theme outer-top-ss">
                <div class="item">
                  <div class="products">
                    <div class="hot-deal-wrapper">
                      <div class="image"> 
                      <a href="#">
                      <img src="assets/images/hot-deals/p13.jpg" alt=""> 
                      <img src="assets/images/hot-deals/p13_hover.jpg" alt="" class="hover-image">
                      </a>
                      </div>
                      <div class="sale-offer-tag"><span>49%<br>
                        off</span></div>
                      <div class="timing-wrapper">
                        <div class="box-wrapper">
                          <div class="date box"> <span class="key">120</span> <span class="value">DAYS</span> </div>
                        </div>
                        <div class="box-wrapper">
                          <div class="hour box"> <span class="key">20</span> <span class="value">HRS</span> </div>
                        </div>
                        <div class="box-wrapper">
                          <div class="minutes box"> <span class="key">36</span> <span class="value">MINS</span> </div>
                        </div>
                        <div class="box-wrapper">
                          <div class="seconds box"> <span class="key">60</span> <span class="value">SEC</span> </div>
                        </div>
                      </div>
                    </div>
                    <!-- /.hot-deal-wrapper -->
                    
                    <div class="product-info text-left m-t-20">
                      <h3 class="name"><a href="detail.html">Floral Print Buttoned</a></h3>
                      <div class="rating rateit-small"></div>
                      <div class="product-price"> <span class="price"> $600.00 </span> <span class="price-before-discount">$800.00</span> </div>
                      <!-- /.product-price --> 
                      
                    </div>
                    <!-- /.product-info -->
                    
                    <div class="cart clearfix animate-effect">
                      <div class="action">
                        <div class="add-cart-button btn-group">
                          <button class="btn btn-primary icon" data-toggle="dropdown" type="button"> <i class="fa fa-shopping-cart"></i> </button>
                          <button class="btn btn-primary cart-btn" type="button">Add to cart</button>
                        </div>
                      </div>
                      <!-- /.action --> 
                    </div>
                    <!-- /.cart --> 
                  </div>
                </div>
                <div class="item">
                  <div class="products">
                    <div class="hot-deal-wrapper">
                      <div class="image"> 
                       <a href="#">
                      <img src="assets/images/hot-deals/p14.jpg" alt=""> 
                      <img src="assets/images/hot-deals/p14_hover.jpg" alt="" class="hover-image">
                      </a>
                       </div>
                      <div class="sale-offer-tag"><span>35%<br>
                        off</span></div>
                      <div class="timing-wrapper">
                        <div class="box-wrapper">
                          <div class="date box"> <span class="key">120</span> <span class="value">Days</span> </div>
                        </div>
                        <div class="box-wrapper">
                          <div class="hour box"> <span class="key">20</span> <span class="value">HRS</span> </div>
                        </div>
                        <div class="box-wrapper">
                          <div class="minutes box"> <span class="key">36</span> <span class="value">MINS</span> </div>
                        </div>
                        <div class="box-wrapper">
                          <div class="seconds box"> <span class="key">60</span> <span class="value">SEC</span> </div>
                        </div>
                      </div>
                    </div>
                    <!-- /.hot-deal-wrapper -->
                    
                    <div class="product-info text-left m-t-20">
                      <h3 class="name"><a href="detail.html">Floral Print Buttoned</a></h3>
                      <div class="rating rateit-small"></div>
                      <div class="product-price"> <span class="price"> $600.00 </span> <span class="price-before-discount">$800.00</span> </div>
                      <!-- /.product-price --> 
                      
                    </div>
                    <!-- /.product-info -->
                    
                    <div class="cart clearfix animate-effect">
                      <div class="action">
                        <div class="add-cart-button btn-group">
                          <button class="btn btn-primary icon" data-toggle="dropdown" type="button"> <i class="fa fa-shopping-cart"></i> </button>
                          <button class="btn btn-primary cart-btn" type="button">Add to cart</button>
                        </div>
                      </div>
                      <!-- /.action --> 
                    </div>
                    <!-- /.cart --> 
                  </div>
                </div>
                <div class="item">
                  <div class="products">
                    <div class="hot-deal-wrapper">
                      <div class="image">
                       <a href="#">
                      <img src="assets/images/hot-deals/p15.jpg" alt=""> 
                      <img src="assets/images/hot-deals/p15_hover.jpg" alt="" class="hover-image">
                      </a>
                       </div>
                      <div class="sale-offer-tag"><span>35%<br>
                        off</span></div>
                      <div class="timing-wrapper">
                        <div class="box-wrapper">
                          <div class="date box"> <span class="key">120</span> <span class="value">Days</span> </div>
                        </div>
                        <div class="box-wrapper">
                          <div class="hour box"> <span class="key">20</span> <span class="value">HRS</span> </div>
                        </div>
                        <div class="box-wrapper">
                          <div class="minutes box"> <span class="key">36</span> <span class="value">MINS</span> </div>
                        </div>
                        <div class="box-wrapper">
                          <div class="seconds box"> <span class="key">60</span> <span class="value">SEC</span> </div>
                        </div>
                      </div>
                    </div>
                    <!-- /.hot-deal-wrapper -->
                    
                    <div class="product-info text-left m-t-20">
                      <h3 class="name"><a href="detail.html">Floral Print Buttoned</a></h3>
                      <div class="rating rateit-small"></div>
                      <div class="product-price"> <span class="price"> $600.00 </span> <span class="price-before-discount">$800.00</span> </div>
                      <!-- /.product-price --> 
                      
                    </div>
                    <!-- /.product-info -->
                    
                    <div class="cart clearfix animate-effect">
                      <div class="action">
                        <div class="add-cart-button btn-group">
                          <button class="btn btn-primary icon" data-toggle="dropdown" type="button"> <i class="fa fa-shopping-cart"></i> </button>
                          <button class="btn btn-primary cart-btn" type="button">Add to cart</button>
                        </div>
                      </div>
                      <!-- /.action --> 
                    </div>
                    <!-- /.cart --> 
                  </div>
                </div>
              </div>
              <!-- /.sidebar-widget --> 
            </div>
    <!-- ============================================== HOT DEALS: END ============================================== -->					
    
    <!-- ============================================== NEWSLETTER ============================================== -->
    <div class="sidebar-widget newsletter outer-bottom-small outer-top-vs">
        <h3 class="section-title">Newsletters</h3>
        <div class="sidebar-widget-body outer-top-xs">
            <p>Sign Up for Our Newsletter!</p>
            <form>
                 <div class="form-group">
                    <label class="sr-only" for="exampleInputEmail1">Email address</label>
                    <input type="email" class="form-control" id="exampleInputEmail1" placeholder="Subscribe to our newsletter">
                  </div>
                <button class="btn btn-primary">Subscribe</button>
            </form>
        </div><!-- /.sidebar-widget-body -->
    </div><!-- /.sidebar-widget -->
    <!-- ============================================== NEWSLETTER: END ============================================== -->
    
    <!-- ============================================== Testimonials============================================== -->
    <div class="sidebar-widget  outer-top-vs ">
        <div id="advertisement" class="advertisement">
            <div class="item">
                <div class="avatar"><img src="assets/images/testimonials/member1.png" alt="Image"></div>
            <div class="testimonials"><em>"</em> Vtae sodales aliq uam morbi non sem lacus port mollis. Nunc condime tum metus eud molest sed consectetuer.<em>"</em></div>
            <div class="clients_author">John Doe	<span>Abc Company</span>	</div><!-- /.container-fluid -->
            </div><!-- /.item -->
    
             <div class="item">
                 <div class="avatar"><img src="assets/images/testimonials/member3.png" alt="Image"></div>
            <div class="testimonials"><em>"</em>Vtae sodales aliq uam morbi non sem lacus port mollis. Nunc condime tum metus eud molest sed consectetuer.<em>"</em></div>
            <div class="clients_author">Stephen Doe	<span>Xperia Designs</span>	</div>    
            </div><!-- /.item -->
    
            <div class="item">
                <div class="avatar"><img src="assets/images/testimonials/member2.png" alt="Image"></div>
            <div class="testimonials"><em>"</em> Vtae sodales aliq uam morbi non sem lacus port mollis. Nunc condime tum metus eud molest sed consectetuer.<em>"</em></div>
            <div class="clients_author">Saraha Smith	<span>Datsun &amp; Co</span>	</div><!-- /.container-fluid -->
            </div><!-- /.item -->
    
        </div><!-- /.owl-carousel -->
    </div>
        
    <!-- ============================================== Testimonials: END ============================================== -->
    
     
    
                    </div>
                </div><!-- /.sidebar -->
          
                <div class='col-xs-12 col-sm-12 col-md-9 rht-col'>
                <div class="detail-block">
                    <div class="row">
                    
                        <div class="col-xs-12 col-sm-12 col-md-4 col-lg-4 gallery-holder">
                            <div class="product-item-holder size-big single-product-gallery small-gallery">
                        
                                <!-- Main product image -->
                                <div id="owl-single-product">
                                    <div class="single-product-gallery-item" id="slide1">
                                        <a data-lightbox="image-1" data-title="Gallery" href="{{ single_product.images.url }}">
                                            {% comment %} <img class="img-responsive" alt="" src="{{ single_product.images.url }}" /> {% endcomment %}
                                            <img class="img-responsive main-product-image" alt="" src="{{ single_product.images.url }}" />

                                        </a>
                                    </div>
                                </div>
                        
                                <!-- Thumbnail images -->
                                <div class="single-product-gallery-thumbs gallery-thumbs">
                                    <div id="owl-single-product-thumbnails">
                                        <div class="item">
                                            <a class="horizontal-thumb {% if forloop.first %}active{% endif %}"
                                               data-target="#owl-single-product" data-slide="main"
                                               href="#slidemain"
                                               data-large-image="{{ single_product.images.url }}"> <!-- Add data-large-image attribute to store the large image URL -->
                                                <img class="img-responsive" alt="" src="{{ single_product.images.url }}" />
                                            </a>
                                        </div>
                                        <div class="item">
                                            <a class="horizontal-thumb {% if forloop.first %}active{% endif %}"
                                               data-target="#owl-single-product" data-slide="main"
                                               href="#slidemain_hover"
                                               data-large-image="{{ single_product.images.url }}"> <!-- Add data-large-image attribute to store the large image URL -->
                                                <img class="img-responsive" alt="" src="{{ single_product.images_hover.url }}" />
                                            </a>
                                        </div>
                                        {% for gallery_image in product_gallery %}
                                            <div class="item">
                                                <a class="horizontal-thumb {% if forloop.first %}active{% endif %}"
                                                   data-target="#owl-single-product" data-slide="{{ forloop.counter }}"
                                                   href="#slide{{ forloop.counter }}"
                                                   data-large-image="{{ gallery_image.image.url }}"> <!-- Add data-large-image attribute to store the large image URL -->
                                                    <img class="img-responsive" alt="" src="{{ gallery_image.image.url }}" />
                                                </a>
                                            </div>
                                        {% endfor %}
                                    </div>
                                </div>
                                <script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>

                                <script>
                                    $(document).ready(function() {
                                        // Handle click event on thumbnail images
                                        $('.horizontal-thumb').on('click', function(e) {
                                            e.preventDefault();
                                    
                                            // Update the main product image source and data-title using the clicked thumbnail's data-large-image and alt attributes
                                            var largeImage = $(this).data('large-image');
                                            var title = $(this).find('img').attr('alt');
                                    
                                            $('.main-product-image').attr('src', largeImage);
                                            $('.main-product-image').attr('data-title', title);
                                    
                                            // You can also update any lightbox or other features you might have
                                            // Example: Trigger lightbox to display the clicked image
                                            $('[data-lightbox="image-1"]').attr('href', largeImage);
                                            $('[data-lightbox="image-1"]').attr('data-title', title);
                                        });
                                    });
                                    </script>
                        
                            </div>
                        </div>
                        	<form  action="{% url 'custom_add_to_cart' single_product.id %}" method="POST">
                                {% csrf_token %}
                        <div class='col-sm-12 col-md-8 col-lg-8 product-info-block'>
                            <div class="product-info">
                                <h1 class="name">{{single_product.product_name}}</h1>
                                
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
                                        {{single_product.description}}
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
</body>

</html>