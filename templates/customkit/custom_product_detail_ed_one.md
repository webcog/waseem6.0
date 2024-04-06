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
<title>{% block title %}{{single_product.product_name}}{% endblock title %} - Tie</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Kdam+Thmor+Pro&family=Kode+Mono:wght@400..700&family=Lilita+One&family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">

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



<script>
  // Define the CSS rules as a string
  const cssRules = `
      #image-display {
          width: 270px;
          height: 350px;
          position: relative;
          border: 2px dashed #aaa;
          overflow: hidden;
      }
      #existing-image, #uploaded-image {
          position: absolute;
          top: 0;
          left: 0;
          max-width: 100%;
          max-height: 100%;
          cursor: pointer; /* Make the images draggable */
          box-sizing: border-box;
      }
      #image-border {
          position: absolute;
          top: -4px;
          left: -4px;
          width: calc(100% + 8px);
          height: calc(100% + 8px);
          border: 4px dashed transparent;
          pointer-events: none; /* Ensures the border doesn't interfere with dragging */
      }
      .text-overlay {
          position: absolute;
          font-size: 18px;
          color: black;
          cursor: pointer;
          font-family: 'Roboto', sans-serif; /* Default font */
      }
  `;

  // Create a style element
  const styleElement = document.createElement('style');

  // Set the CSS rules
  styleElement.textContent = cssRules;

  // Append the style element to the head of the document
  document.head.appendChild(styleElement);
</script>


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
                            <div id="image-display">
                                <img id="existing-image" class="img-responsive main-product-image" alt="" src="{{ single_product.images.url }}" />
                                <img id="uploaded-image" style="display: none;">
                                <div id="image-border"></div>
                            </div>
                        </div>
                    </div>

                    <div class='col-sm-12 col-md-8 col-lg-8 product-info-block'>
                      <form  action="{% url 'custom_add_to_cart' single_product.id %}" method="POST">
                        {% csrf_token %}
                      
                          


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
                                <hr>
                                <div>
                                  <input type="radio" class="" checked>
                                  <label for=""  class="form-label">Create Your Own Desing</label>
                                </div>
                                <div class="" style="margin-bottom: 10px;margin-top: 10px;">
                                  <input type="text" class="form-control" id="text-input" placeholder="Type text here">
                                </div>
                               
                                

                                <div class="row">
                                  <div class="col-md-3">
                                    <input class="form-control" type="color" id="color-picker" value="#000000">
                                  </div>
                                  <div class="col-md-9">
                                    <select id="font-dropdown" class="form-control">
                                      <option value="Arial">Arial</option>
                                      <option value=""Kdam Thmor Pro", sans-serif" style="font-family: 'Kdam Thmor Pro', sans-serif;">Kdam Thmor Pro</option>
                                    
                                      <option value="'Kode Mono', sans-serif" style="font-family: 'Kode Mono', monospace;">Kode Mono</option>
                                      <option value="'Lilita One', sans-serif" style=" font-family: 'Lilita One', sans-serif;">Lilita One</option>
                                      <option value="'Montserrat', sans-serif" style="  font-family: 'Montserrat', sans-serif;">Montserrat</option>
                                    </select>
                                  </div>
                                </div>

                                <div style="margin-top: 10px;">
                              
                                  <input type="file" id="file-input" class="">
                                </div>
    
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
    
                                        <div class="col-sm-6 col-xs-6">

                                        {% if single_product.stock <= 0 %} 
                                        {% else %}
                                        <div class="add-btn" style="margin-top: 15px;">
                                          <button type="submit"  class="btn btn-primary"><i class="fa fa-shopping-cart inner-right-vs"></i> ADD TO CART</button>
                                      </div>
        
                                        {% endif %}

                                      </div>

                                    </div><!-- /.row -->
                                </div><!-- /.price-container -->

                             
                                
                                
    
                               
    
                                
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









<script>
  // JavaScript logic for image display with overlay
  let uploadedImage;
  let resizeHandle;
  let selectedElement;

  function displayUploadedImage() {
      const reader = new FileReader();
      reader.onload = function(e) {
          const img = new Image();
          img.src = e.target.result;
          img.onload = function() {
              const existingImage = document.getElementById('existing-image');
              const uploadedImageElement = document.getElementById('uploaded-image');
              const imageDisplay = document.getElementById('image-display');

              uploadedImageElement.style.display = 'none';

              uploadedImageElement.src = img.src;
              uploadedImageElement.style.display = 'block';

              const aspectRatio = img.width / img.height;
              let width = imageDisplay.offsetWidth / 2; // Default width
              let height = width / aspectRatio;

              if (height > imageDisplay.offsetHeight) {
                  height = imageDisplay.offsetHeight / 2;
                  width = height * aspectRatio;
              }

              const offsetX = (imageDisplay.offsetWidth - width) / 2;
              const offsetY = (imageDisplay.offsetHeight - height) / 2;

              uploadedImageElement.style.width = width + 'px';
              uploadedImageElement.style.height = height + 'px';
              uploadedImageElement.style.left = offsetX + 'px';
              uploadedImageElement.style.top = offsetY + 'px';

              // Save uploaded image details for further manipulation
              uploadedImage = {
                  offsetX,
                  offsetY,
                  width,
                  height
              };

              // Make the uploaded image draggable
              uploadedImageElement.addEventListener('mousedown', startDragging);
              document.addEventListener('mouseup', stopDragging);

              // Add resize handles
              addResizeHandles();
          };
      };
      reader.readAsDataURL(document.getElementById('file-input').files[0]);
  }

  // Add resize handles to the image
  function addResizeHandles() {
      const imageDisplay = document.getElementById('image-display');
      const border = document.getElementById('image-border');
      const uploadedImageElement = document.getElementById('uploaded-image');

      const handles = ['nw', 'ne', 'sw', 'se'];
      for (let i = 0; i < handles.length; i++) {
          const handle = document.createElement('div');
          handle.className = 'border-handle ' + handles[i];
          handle.addEventListener('mousedown', startResizing);
          border.appendChild(handle);
      }

      // Adjust border size and position
      border.style.width = uploadedImageElement.offsetWidth + 'px';
      border.style.height = uploadedImageElement.offsetHeight + 'px';
      border.style.left = uploadedImageElement.offsetLeft - 4 + 'px';
      border.style.top = uploadedImageElement.offsetTop - 4 + 'px';
  }

  // Variables to track mouse movements during dragging
  let initialX, initialY, offsetX = 0, offsetY = 0;
  let isDragging = false;

  function startDragging(e) {
      if (e.target.id === 'uploaded-image') { // Check if the target is the image
          isDragging = true;
          selectedElement = e.target;
          initialX = e.clientX - selectedElement.offsetLeft;
          initialY = e.clientY - selectedElement.offsetTop;
      }
  }

  function stopDragging() {
      isDragging = false;
  }

  function drag(e) {
      if (isDragging) {
          e.preventDefault();
          const x = e.clientX - initialX;
          const y = e.clientY - initialY;
          offsetX = x;
          offsetY = y;
          selectedElement.style.left = offsetX + 'px';
          selectedElement.style.top = offsetY + 'px';

          // Update border position if image is dragged
          if (selectedElement.id === 'uploaded-image') {
              const border = document.getElementById('image-border');
              border.style.left = selectedElement.offsetLeft - 4 + 'px';
              border.style.top = selectedElement.offsetTop - 4 + 'px';
          }
      }
  }

  // Variables to track resizing
  let isResizing = false;
  let resizeDirection;

  function startResizing(e) {
      if (e.button === 0) { // Check if the left mouse button is pressed
          isResizing = true;
          resizeHandle = e.target;
          initialX = e.clientX;
          initialY = e.clientY;
          const rect = uploadedImage.getBoundingClientRect();
          offsetX = rect.left;
          offsetY = rect.top;
          resizeDirection = resizeHandle.className.split(' ')[1];
      }
  }

  function stopResizing() {
      isResizing = false;
  }

  function resize(e) {
      if (isResizing) {
          e.preventDefault();
          const widthChange = e.clientX - initialX;
          const heightChange = e.clientY - initialY;

          let newWidth = uploadedImage.width + widthChange;
          let newHeight = uploadedImage.height + heightChange;

          switch (resizeDirection) {
              case 'nw':
                  uploadedImage.style.width = newWidth + 'px';
                  uploadedImage.style.height = newHeight + 'px';
                  uploadedImage.style.left = offsetX + widthChange + 'px';
                  uploadedImage.style.top = offsetY + heightChange + 'px';
                  break;
              case 'ne':
                  uploadedImage.style.width = newWidth + 'px';
                  uploadedImage.style.height = newHeight + 'px';
                  uploadedImage.style.top = offsetY + heightChange + 'px';
                  break;
              case 'sw':
                  uploadedImage.style.width = newWidth + 'px';
                  uploadedImage.style.height = newHeight + 'px';
                  uploadedImage.style.left = offsetX + widthChange + 'px';
                  break;
              case 'se':
                  uploadedImage.style.width = newWidth + 'px';
                  uploadedImage.style.height = newHeight + 'px';
                  break;
          }

          // Update border size
          const border = document.getElementById('image-border');
          border.style.width = newWidth + 'px';
          border.style.height = newHeight + 'px';
      }
  }

  function changeFont() {
      const fontSelect = document.getElementById('font-dropdown');
      const selectedFont = fontSelect.options[fontSelect.selectedIndex].value;
      const textElements = document.querySelectorAll('.text-overlay');
      textElements.forEach(element => {
          element.style.fontFamily = selectedFont;
      });
  }

  function changeTextColor() {
      const color = document.getElementById('color-picker').value;
      const textElements = document.querySelectorAll('.text-overlay');
      textElements.forEach(element => {
          element.style.color = color;
      });
  }

  function addTextToImage() {
      const text = document.getElementById('text-input').value;
      const imageDisplay = document.getElementById('image-display');

      // Remove existing text elements
      const existingTextElements = document.querySelectorAll('.text-overlay');
      existingTextElements.forEach(element => {
          imageDisplay.removeChild(element);
      });

      // Add new text element
      const textElement = document.createElement('div');
      textElement.innerText = text;
      textElement.className = 'text-overlay';
      textElement.style.top = '50%';
      textElement.style.left = '50%';
      textElement.style.transform = 'translate(-50%, -50%)';

      // Make the text draggable only when clicking on the text
      textElement.addEventListener('mousedown', function(e) {
          if (e.target.classList.contains('text-overlay')) {
              isDragging = true;
              selectedElement = e.target;
              initialX = e.clientX - selectedElement.offsetLeft;
              initialY = e.clientY - selectedElement.offsetTop;
          }
      });

      imageDisplay.appendChild(textElement);

      // Event listeners for dragging the text
      document.addEventListener('mouseup', stopDragging);
      document.addEventListener('mousemove', drag);
  }

  function initialize() {
      document.getElementById('file-input').addEventListener('change', displayUploadedImage);

      document.getElementById('image-display').addEventListener('dragstart', function(event) {
          event.preventDefault();
      });

      document.getElementById('image-display').addEventListener('dragover', function(event) {
          event.preventDefault();
      });

      document.getElementById('image-display').addEventListener('drop', function(event) {
          event.preventDefault();
      });

      document.getElementById('text-input').addEventListener('input', addTextToImage);

      document.getElementById('font-dropdown').addEventListener('change', changeFont);

      document.getElementById('color-picker').addEventListener('input', changeTextColor);

      document.addEventListener('mousemove', resize);
      document.addEventListener('mouseup', stopResizing);
  }

  document.addEventListener('DOMContentLoaded', initialize);
</script>


</body>

</html>