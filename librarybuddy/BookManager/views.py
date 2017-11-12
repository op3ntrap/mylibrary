# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Book
from silk.profiling.profiler import silk_profile


@silk_profile(name='archive_catalog_view')
def archive_catalog(request):
	catalog_list = Book.objects.all()
	# section = []
	# i = 0
	# max = len(catalog_list[0:5])
	# while(i<max):
	#     i_i = i+3
	#     if i+3 >=max:
	#         i_i = max-1
	#         section.append(catalog_list[i:i_i])
	#         break
	#     section.append(catalog_list[i:i_i])
	# section = catalog_list[0]
	param = ""
	if request.method == 'GET':
		# Search bar
		try:
			available_param = request.GET["available"]
			if available_param == "True":
				catalog_list = catalog_list.filter(is_available=True)
			elif available_param == "False":
				catalog_list = catalog_list.filter(is_available=False)
		except:
			pass
		# Drip
		try:
			param = request.GET["search_book"]
			if " " in param:
				param_list = param.split(" ")
				for val in param_list:
					catalog_list += Book.objects.filter(title__icontains=val)
					catalog_list += Book.objects.filter(description__icontains=val)


			else:
				catalog_list = Book.objects.filter(title__icontains=param)
				catalog_list += Book.objects.filter(description__icontains=param)

		except:
			a = ""

	input_param = param
	context = {'sections': catalog_list, "input_param": input_param}
	# Send out 3 sets of all the books available

	return render(request, 'BookManager/archive_catalog.html', context)


@silk_profile
def view_base_template(request):
	return render(request, 'BookManager/account_management.html', context=None)


"""
{#        <!--Page Custom-->#}
{##}
{#        {% if sections %}#}
{#            {% for section in sections %}#}
{#                <!--row-->#}
{#                <div class="row mt-5 wow">#}
{#                {% for card in section %}#}
{##}
{#                    <!--Card-->#}
{#                    <div class="col-lg-4 wow fadeIn" data-wow-delay="0.2s">#}
{#                        <div class="card">#}
{##}
{#                            <!--Card image-->#}
{#                            <img class="img-fluid"#}
{#                                 src="https://mdbootstrap.com/img/Photos/Horizontal/Food/4-col/img%20(43).jpg"#}
{#                                 alt="Card image cap">#}
{##}
{#                            <!--Card content-->#}
{#                            <div class="card-body">#}
{#                                <!--Title-->#}
{#                                <h4 class="card-title">Card title</h4>#}
{#                                <!--Text-->#}
{#                                <p class="card-text">Some quick example text to build on the card title and make up the#}
{#                                    bulk of#}
{#                                    the card's content.</p>#}
{#                                <a href="#" class="btn btn-primary">Button</a>#}
{#                            </div>#}
{##}
{#                        </div>#}
{#                    </div>#}
{#                    <!--/.Card-->#}
{##}
{#                {% endfor %}#}
{#                </div>#}
{#            {% endfor %}#}
{#        {% else %}#}
{#            <p>No polls are available.</p>#}
{#        {% endif %}#}
{#    <!--Page Custom-->#}
"""


@silk_profile
def test(request):
	return render(request, 'BookManager/account_management.html', context=None)
