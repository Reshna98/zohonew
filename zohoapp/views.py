from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.utils.text import capfirst
from django.contrib.auth.models import User,auth
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

from .models import Attach
from django.contrib.auth.models import User
from .models import Expense

def index(request):

    return render(request,'index.html')

def register(request):
   
    if request.method=='POST':

        first_name=capfirst(request.POST['fname'])
        last_name=capfirst(request.POST['lname'])
        username=request.POST['uname']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email1']
        phone = request.POST['phone']

      
        if password==cpassword:  #  password matching......
            if User.objects.filter(username=username).exists(): #check Username Already Exists..
                messages.info(request, 'This username already exists!!!!!!')
                return redirect('register')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email)
                
                user.save()
                u = User.objects.get(id = user.id)

                company_details(contact_number = phone, user = u).save()
    
        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            print("Password is not Matching.. ") 
            return redirect('register')   
        return redirect('register')

    return render(request,'register.html')

def login(request):
        
    if request.method == 'POST':
        
        email_or_username = request.POST['emailorusername']
        password = request.POST['password']

        user = authenticate(request, username=email_or_username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('base')
        else:
            return redirect('/')

    return render(request, 'register.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='login')
def base(request):
   
    
    company = company_details.objects.get(user = request.user)
    context = {
                'company' : company
            }
    return render(request,'loginhome.html',context)

@login_required(login_url='login')
def view_profile(request):

    company = company_details.objects.get(user = request.user)
    context = {
                'company' : company
            }
    return render(request,'profile.html',context)

@login_required(login_url='login')
def edit_profile(request,pk):

    company = company_details.objects.get(id = pk)
    user1 = User.objects.get(id = company.user_id)

    if request.method == "POST":

        user1.first_name = capfirst(request.POST.get('f_name'))
        user1.last_name  = capfirst(request.POST.get('l_name'))
        user1.username = request.POST.get('uname')
        # pat.age = request.POST.get('age')
        # pat.address = capfirst(request.POST.get('address'))
        # pat.gender = request.POST.get('gender')
        # user1.email = request.POST.get('email')
        # pat.email = request.POST.get('email')
        # pat.contact_num = request.POST.get('cnum')
        # #fkey1= request.POST.get('doc')
        # #pat.doctor = doctor.objects.get(id = fkey1)
        # if len(request.FILES)!=0 :
        #     doc.profile_pic = request.FILES.get('file')


        company.save()
        user1.save()
        return redirect('view_profile')

    context = {
        'company' : company,
        'user1' : user1,
    }
    context = {
                'company' : company,
            }
    return render(request,'edit_profile.html',context)

@login_required(login_url='login')
def itemview(request):
    viewitem=AddItem.objects.all()
    return render(request,'item_view.html',{'view':viewitem})


@login_required(login_url='login')
def additem(request):
    unit=Unit.objects.all()
    sale=Sales.objects.all()
    purchase=Purchase.objects.all()
    
    


  
    
        



    accounts = Purchase.objects.all()
    account_types = set(Purchase.objects.values_list('Account_type', flat=True))

    
    account = Sales.objects.all()
    account_type = set(Sales.objects.values_list('Account_type', flat=True))
    
    

    return render(request,'additem.html',{'unit':unit,'sale':sale,'purchase':purchase,
               
                            "account":account,"account_type":account_type,"accounts":accounts,"account_types":account_types,
                            
                            })

@login_required(login_url='login')
def add_account(request):
    if request.method=='POST':
        Account_type  =request.POST['acc_type']
        Account_name =request.POST['acc_name']
        Acount_code =request.POST['acc_code']
        Account_desc =request.POST['acc_desc']
       
        acc=Purchase(Account_type=Account_type,Account_name=Account_name,Acount_code=Acount_code,Account_desc=Account_desc)
        acc.save()                 
        return redirect("additem")
        
    return render(request,'additem.html')


@login_required(login_url='login')
def add(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            radio=request.POST.get('radio')
            if radio=='tax':
    
                
                inter=request.POST['inter']
                intra=request.POST['intra']
                type=request.POST.get('type')
                name=request.POST['name']
                unit=request.POST['unit']
                sel_price=request.POST.get('sel_price')
                sel_acc=request.POST.get('sel_acc')
                s_desc=request.POST.get('sel_desc')
                cost_price=request.POST.get('cost_price')
                cost_acc=request.POST.get('cost_acc')      
                p_desc=request.POST.get('cost_desc')
                u=request.user.id
                us=request.user
                history="Created by" + str(us)
                user=User.objects.get(id=u)
                unit=Unit.objects.get(id=unit)
                sel=Sales.objects.get(id=sel_acc)
                cost=Purchase.objects.get(id=cost_acc)
                ad_item=AddItem(type=type,Name=name,p_desc=p_desc,s_desc=s_desc,s_price=sel_price,p_price=cost_price,unit=unit,
                            sales=sel,purchase=cost,user=user,creat=history,interstate=inter,intrastate=intra
                                )
                
            else:
                                                  
                type=request.POST.get('type')
                name=request.POST['name']
                unit=request.POST['unit']
                sel_price=request.POST.get('sel_price')
                sel_acc=request.POST.get('sel_acc')
                s_desc=request.POST.get('sel_desc')
                cost_price=request.POST.get('cost_price')
                cost_acc=request.POST.get('cost_acc')      
                p_desc=request.POST.get('cost_desc')
                u=request.user.id
                us=request.user
                history="Created by" + str(us)
                user=User.objects.get(id=u)
                unit=Unit.objects.get(id=unit)
                sel=Sales.objects.get(id=sel_acc)
                cost=Purchase.objects.get(id=cost_acc)
                ad_item=AddItem(type=type,Name=name,p_desc=p_desc,s_desc=s_desc,s_price=sel_price,p_price=cost_price,unit=unit,
                            sales=sel,purchase=cost,user=user,creat=history,interstate='none',intrastate='none'
                                )
                ad_item.save()
            ad_item.save()
           
            return redirect("itemview")
    return render(request,'additem.html')



@login_required(login_url='login')
def edititem(request,id):
    pedit=AddItem.objects.get(id=id)
    p=Purchase.objects.all()
    s=Sales.objects.all()
    u=Unit.objects.all()

    accounts = Purchase.objects.all()
    account_types = set(Purchase.objects.values_list('Account_type', flat=True))
    

    
    account = Sales.objects.all()
    account_type = set(Sales.objects.values_list('Account_type', flat=True))
    
    return render(request,'edititem.html',{"account":account,"account_type":account_type,'e':pedit,'p':p,'s':s,'u':u,"accounts":accounts,"account_types":account_types})


@login_required(login_url='login')
def edit_db(request,id):
        if request.method=='POST':
            edit=AddItem.objects.get(id=id)
            edit.type=request.POST.get('type')
            edit.Name=request.POST['name']
            unit=request.POST['unit']
            edit.s_price=request.POST['sel_price']
            sel_acc=request.POST['sel_acc']
            edit.s_desc=request.POST['sel_desc']
            edit.p_price=request.POST['cost_price']
            cost_acc=request.POST['cost_acc']        
            edit.p_desc=request.POST['cost_desc']
            
            
            edit.unit=Unit.objects.get(id=unit)
            edit.sales=Sales.objects.get(id=sel_acc)
            edit.purchase=Purchase.objects.get(id=cost_acc)
            edit.save()
            return redirect('itemview')

        return render(request,'edititem.html')


@login_required(login_url='login')
def detail(request,id):
    user_id=request.user
    items=AddItem.objects.all()
    product=AddItem.objects.get(id=id)
    history=History.objects.filter(p_id=product.id)
    print(product.id)
    
    
    context={
       "allproduct":items,
       "product":product,
       "history":history,
      
    }
    
    return render(request,'demo.html',context)


@login_required(login_url='login')
def Action(request,id):
    user=request.user.id
    user=User.objects.get(id=user)
    viewitem=AddItem.objects.all()
    event=AddItem.objects.get(id=id)
    

    print(user)
    if request.method=='POST':
        action=request.POST['action']
        event.satus=action
        event.save()
        if action == 'active':
            History(user=user,message="Item marked as Active ",p=event).save()
        else:
            History(user=user,message="Item marked as inActive",p=event).save()
    return render(request,'item_view.html',{'view':viewitem})

@login_required(login_url='login')
def cleer(request,id):
    dl=AddItem.objects.get(id=id)
    dl.delete()
    return redirect('itemview')


@login_required(login_url='login')
def add_unit(request):
    if request.method=='POST':
        unit_name=request.POST['unit_name']
        Unit(unit=unit_name).save()
        return redirect('additem')
    return render(request,"additem.html")


@login_required(login_url='login')
def add_sales(request):
    if request.method=='POST':
        Account_type  =request.POST['acc_type']
        Account_name =request.POST['acc_name']
        Acount_code =request.POST['acc_code']
        Account_desc =request.POST['acc_desc']        
        acc=Sales(Account_type=Account_type,Account_name=Account_name,Acount_code=Acount_code,Account_desc=Account_desc)
        acc.save()
        return redirect('additem')
    return render(request,'additem.html')

def expensepage(request):
    expenses = Expense.objects.filter(user=request.user)
    context = {
        'expenses': expenses,
       }
    return render(request,'expense.html',context)


# def save_expense(request):
#     c= addcustomer.objects.all()
#     if request.method == 'POST':
#         date = request.POST.get('date')
#         select=request.POST['select']
#         expense_account=Account.objects.get(id=select)
#         amount = request.POST.get('amount')
#         currency = request.POST.get('currency')
#         expense_type = request.POST.get('expense_type')
#         paid = request.POST.get('paid')
#         vendor = request.POST.get('vendor')
#         notes = request.POST.get('notes')
#         if request.POST.get('expense_type') == 'goods':
#             hsn_code = request.POST.get('sac')
#             sac = request.POST.get('hsn_code')
#         else:
#             hsn_code = request.POST.get('hsn_code')
#             sac = request.POST.get('sac')
#         attachment_file = request.FILES.get('attachment')
#         gst_treatment = request.POST.get('gst_treatment')
#         destination_of_supply = request.POST.get('destination_of_supply')
#         reverse_charge = request.POST.get('reverse_charge',False)
#         tax = request.POST.get('tax')
#         invoice = request.POST.get('invoice')
#         # customer_id= request.POST.get('customer_id')
#         # customer = addcustomer.objects.get(id=customer_id)
#         c=request.POST['c_name']
#         cus=addcustomer.objects.get(customer_id=c)  
#         # custo=cus.id
#         reporting_tags = request.POST.get('reporting_tags')
#         taxamt=request.POST.get('taxamt',False)
#         expense = Expense.objects.create(
#             user=request.user,
#             date=date,
#             expense_account=expense_account,
#             amount=amount,
#             currency=currency,
#             taxamt=taxamt,
#             sac=sac,
#             expense_type=expense_type,
#             paid=paid,
#             vendor=vendor,
#             notes=notes,
#             hsn_code=hsn_code,
#             gst_treatment=gst_treatment,
#             destination_of_supply=destination_of_supply,
#             reverse_charge=reverse_charge,
#             tax=tax,
#             invoice=invoice,
#             customer_name=cus,
#             reporting_tags=reporting_tags,
#             attachment_file = attachment_file 
#         )

#         expense.save()

#         return redirect('expensepage')  
    
#     return render(request, 'addexpense.html',{'customer':c}) 
def save_expense(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
           
            date = request.POST.get('date')
            select = request.POST['select']
            expense_account = Account.objects.get(id=select)
            amount = request.POST.get('amount')
            currency = request.POST.get('currency')
            expense_type = request.POST.get('expense_type')
            paid = request.POST.get('paid')
            # vendor = request.POST.get('vendor')
            notes = request.POST.get('notes')
            if request.POST.get('expense_type') == 'goods':
                hsn_code = request.POST.get('sac')
                sac = request.POST.get('hsn_code')
            else:
                hsn_code = request.POST.get('hsn_code')
                sac = request.POST.get('sac')
            # attachment_file = request.FILES.get('attachment')
            gst_treatment = request.POST.get('gst_treatment')
            destination_of_supply = request.POST.get('destination_of_supply')
            reverse_charge = request.POST.get('reverse_charge',False)
            tax = request.POST.get('tax')
            invoice = request.POST.get('invoice')
            # c = request.POST['c_name']
            c = request.POST.get('customer')
            customer = addcustomer.objects.get(customer_name=c)
           
        
            v= request.POST.get('vendor')
            vendor=vendor_table.objects.get(vendor_display_name=v)

            # customer = addcustomer.objects.get(customer_id=c)
            taxamt = request.POST.get('taxamt', False)
            # reporting_tags=request.post.get('retag')
            image = request.FILES.get('image')
            # if 'image' in request.FILES:
            #     image = request.FILES['image']  # Set the uploaded image
            # else:
            #     image = None  


            expense = Expense.objects.create(
                user=request.user,
                date=date,
                image=image,
                expense_account=expense_account,
                amount=amount,
                currency=currency,
                taxamt=taxamt,
                sac=sac,
                expense_type=expense_type,
                paid=paid,
                # reporting_tags=reporting_tags,
                notes=notes,
                hsn_code=hsn_code,
                gst_treatment=gst_treatment,
                destination_of_supply=destination_of_supply,
                reverse_charge=reverse_charge,
                tax=tax,
                invoice=invoice,
                customer_name= customer,
                vendor=vendor
                # attachment_file=attachment_file
            )

            expense.save()

            return redirect('expensepage')
        else:
            # Display the save_expense form
            c = addcustomer.objects.all()
            v=vendor_table.objects.all()
            accounts = Account.objects.all()
            account_types = set(Account.objects.values_list('type', flat=True))
           
          
            return render(request, 'addexpense.html', {'vendor':v,'customer': c, 'accounts': accounts, 'account_types': account_types,
            })
   
def upload_documents(request, expense_id):
    if request.method == 'POST':
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        expense = Expense.objects.get(id=expense_id)
        attachment_file = request.FILES.get('attachment')

        doc_data = Attach.objects.create(user=user, expense=expense, attachment=attachment_file)
        doc_data.save()

        return redirect("expense_details", pk=expense.pk)

def add_accountE(request):
    user = User.objects.get(id=request.user.id)

    accounts = Account.objects.all()
    account_types = set(Account.objects.values_list('type', flat=True))
    if request.method == 'POST':
        type = request.POST.get('type')
        name = request.POST.get('name')
        code = request.POST.get('code')
        pname = request.POST.get('pname')
        description=request.POST.get('description')
        new_account = Account(user=user,type=type,name=name,code=code,pname=pname,description=description)
        account_dropdown(request)
        new_account.save()
        # accounts = Account.objects.all()
    return HttpResponse('Account saved successfully')
    return render(request, 'addexpense.html', {
        'accounts': accounts,
        'account_types': account_types,
    })

def account_dropdown(request):
    user = User.objects.get(id=request.user.id)

    options = {}
    account_objects = Account.objects.filter(user=user)
    for account in account_objects:
        # options[account.id] = account.name
        options[account.id] = {
            'name': account.name,
            'type': account.type
        }

    return JsonResponse(options)      
       


def expense_details(request, pk):
    user = request.user
    expense=Expense.objects.all()
    expense_account=Expense.objects.get(id=pk)
    context = {
        'expenses': expense,
        'expense': expense_account,
    }
    return render(request, 'expenseview.html', context)


def entr_custmr(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            type=request.POST.get('type')
            txtFullName=request.POST['txtFullName']
            cpname=request.POST['cpname']
           
            email=request.POST.get('myEmail',None)
            wphone=request.POST.get('wphone',None)
            mobile=request.POST.get('mobile',None)
            skname=request.POST.get('skname',None)
            desg=request.POST.get('desg',None)      
            dept=request.POST.get('dept',None)
            wbsite=request.POST.get('wbsite',None)

            gstt=request.POST.get('gstt',None)
            posply=request.POST.get('posply',None)
            tax1=request.POST.get('tax1',None)
            crncy=request.POST.get('crncy',None)
            obal=request.POST.get('obal')
            obal = int(obal) if obal and obal.strip() else 0 

          
            # select=request.POST.get('pterms')
            # pterms=payment_terms.objects.get(id=select)
            # pterms=request.POST.get('pterms')
            select = request.POST.get('pterms')
            
            try:
                pterms = payment_terms.objects.get(id=select)
            except payment_terms.DoesNotExist:
                pterms = None

            plst=request.POST.get('plst',None)
            plang=request.POST.get('plang',None)
            fbk=request.POST.get('fbk',None)
            twtr=request.POST.get('twtr',None)
        
            atn=request.POST.get('atn',None)
            ctry=request.POST.get('ctry',None)
            
            addrs=request.POST.get('addrs',None)
            addrs1=request.POST.get('addrs1',None)
            bct=request.POST.get('bct',None)
            bst=request.POST.get('bst',None)
            bzip=request.POST.get('bzip',None)
            bpon=request.POST.get('bpon',None)
            bfx=request.POST.get('bfx',None)

            sal=request.POST.get('sal',None)
            ftname=request.POST.get('ftname',None)
            ltname=request.POST.get('ltname',None)
            mail=request.POST.get('mail',None)
            bworkpn=request.POST.get('bworkpn',None)
            bmobile=request.POST.get('bmobile',None)

            bskype=request.POST.get('bskype',None)
            bdesg=request.POST.get('bdesg',None)
            bdept=request.POST.get('bdept',None)
            u = User.objects.get(id = request.user.id)

          
            ctmr=addcustomer(customer_name=txtFullName,customerType=type,
                        companyName=cpname,customerEmail=email,customerWorkPhone=wphone,
                         customerMobile=mobile,skype=skname,designation=desg,department=dept,
                           website=wbsite,GSTTreatment=gstt,placeofsupply=posply, Taxpreference=tax1,
                             currency=crncy,OpeningBalance=obal, PaymentTerms=pterms,
                                PriceList=plst,PortalLanguage=plang,Facebook=fbk,Twitter=twtr,
                                 Attention=atn,country=ctry,Address1=addrs,Address2=addrs1,
                                  city=bct,state=bst,zipcode=bzip,phone1=bpon,
                                   fax=bfx,CPsalutation=sal,Firstname=ftname,
                                    Lastname=ltname,CPemail=mail,CPphone=bworkpn,
                                    CPmobile= bmobile,CPskype=bskype,CPdesignation=bdesg,
                                     CPdepartment=bdept,user=u )
            ctmr.save()  
           
            return redirect('save_expense')
        return render(request, 'addcustomer.html')




def payment_term(request):
    if request.method=='POST':
        term=request.POST.get('term',None)
        day=request.POST.get('day',None)
        ptr=payment_terms(Terms=term,Days=day)
        ptr.save()
        return redirect("entr_custmr")

@login_required(login_url='login')
def add_vendor(request):
    if request.method == "POST":
        vendor_data = vendor_table()
        vendor_data.salutation = request.POST.get('salutation')
        vendor_data.first_name = request.POST.get('first_name')
        vendor_data.last_name = request.POST.get('last_name')
        vendor_data.company_name = request.POST.get('company_name')
        vendor_data.vendor_display_name = request.POST.get('v_display_name')
        vendor_data.vendor_email = request.POST.get('vendor_email')
        vendor_data.vendor_wphone = request.POST.get('w_phone')
        vendor_data.vendor_mphone = request.POST.get('m_phone')
        vendor_data.skype_number = request.POST.get('skype_number')
        vendor_data.designation = request.POST.get('designation')
        vendor_data.department = request.POST.get('department')
        vendor_data.website = request.POST.get('website')
        vendor_data.gst_treatment = request.POST.get('gst')

        x = request.POST.get('gst')
        if x == "Unregistered Business-not Registered under GST":
            vendor_data.pan_number = request.POST.get('pan_number')
            vendor_data.gst_number = None
        else:
            vendor_data.gst_number = request.POST.get('gst_number')
            vendor_data.pan_number = request.POST.get('pan_number')

        vendor_data.source_supply = request.POST.get('source_supply')
        vendor_data.currency = request.POST.get('currency')
        vendor_data.opening_bal = request.POST.get('opening_bal')
        vendor_data.payment_terms = request.POST.get('payment_terms')

        user_id=request.user.id
        udata=User.objects.get(id=user_id)
        vendor_data.user=udata
        vendor_data.battention=request.POST.get('battention')
        vendor_data.bcountry=request.POST.get('bcountry')
        vendor_data.baddress=request.POST.get('baddress')
        vendor_data.bcity=request.POST.get('bcity')
        vendor_data.bstate=request.POST.get('bstate')
        vendor_data.bzip=request.POST.get('bzip')
        vendor_data.bphone=request.POST.get('bphone')
        vendor_data.bfax=request.POST.get('bfax')

        vendor_data.sattention=request.POST.get('sattention')
        vendor_data.scountry=request.POST.get('scountry')
        vendor_data.saddress=request.POST.get('saddress')
        vendor_data.scity=request.POST.get('scity')
        vendor_data.sstate=request.POST.get('sstate')
        vendor_data.szip=request.POST.get('szip')
        vendor_data.sphone=request.POST.get('sphone')
        vendor_data.sfax=request.POST.get('sfax')
        vendor_data.save()
# .......................................................adding to remaks table.....................
        vdata=vendor_table.objects.get(id=vendor_data.id)
        vendor=vdata
        rdata=remarks_table()
        rdata.remarks=request.POST.get('remark')
        rdata.user=udata
        rdata.vendor=vdata
        rdata.save()


#  ...........................adding multiple rows of table to model  ........................................................       
        salutation =request.POST.getlist('salutation[]')
        first_name =request.POST.getlist('first_name[]')
        last_name =request.POST.getlist('last_name[]')
        email =request.POST.getlist('email[]')
        work_phone =request.POST.getlist('wphone[]')
        mobile =request.POST.getlist('mobile[]')
        skype_number =request.POST.getlist('skype[]')
        designation =request.POST.getlist('designation[]')
        department =request.POST.getlist('department[]') 
        vdata=vendor_table.objects.get(id=vendor_data.id)
        vendor=vdata
       

        if len(salutation)==len(first_name)==len(last_name)==len(email)==len(work_phone)==len(mobile)==len(skype_number)==len(designation)==len(department):
            mapped2=zip(salutation,first_name,last_name,email,work_phone,mobile,skype_number,designation,department)
            mapped2=list(mapped2)
            print(mapped2)
            for ele in mapped2:
                created = contact_person_table.objects.get_or_create(salutation=ele[0],first_name=ele[1],last_name=ele[2],email=ele[3],
                         work_phone=ele[4],mobile=ele[5],skype_number=ele[6],designation=ele[7],department=ele[8],user=udata,vendor=vendor)
        response_data = {
            'success': True
        }
        return JsonResponse(response_data)

        # return redirect('save_expense')
    return render(request, 'addvendor.html')

def edit_expense(request,expense_id):
    if request.user.is_authenticated:
        expense = Expense.objects.get(id=expense_id)

        if request.method == 'POST':
            date = request.POST.get('date')
            select = request.POST['select']
            expense_account = Account.objects.get(id=select)
            amount = request.POST.get('amount')
            currency = request.POST.get('currency')
            expense_type = request.POST.get('expense_type')
            paid = request.POST.get('paid')
            notes = request.POST.get('notes')
            if request.POST.get('expense_type') == 'goods':
                hsn_code = request.POST.get('sac')
                sac = request.POST.get('hsn_code')
            else:
                hsn_code = request.POST.get('hsn_code')
                sac = request.POST.get('sac')
            gst_treatment = request.POST.get('gst_treatment')
            destination_of_supply = request.POST.get('destination_of_supply')
            reverse_charge = request.POST.get('reverse_charge', False)
            tax = request.POST.get('tax')
            invoice = request.POST.get('invoice')
            c = request.POST.get('customer')
            customer = addcustomer.objects.get(customer_name=c)
            v = request.POST.get('vendor')
            vendor = vendor_table.objects.get(vendor_display_name=v)
            reporting_tags = request.POST.get('reporting_tags')
            taxamt = request.POST.get('taxamt', False)
            image = request.FILES.get('image')
            # if 'image' in request.FILES:
            #     image = request.FILES['image']  # Set the uploaded image
            # else:
            #     image = None 
            expense.date = date
            expense.expense_account = expense_account
            expense.amount = amount
            expense.currency = currency
            expense.taxamt = taxamt
            expense.sac = sac
            expense.expense_type = expense_type
            expense.paid = paid
            expense.notes = notes
            expense.hsn_code = hsn_code
            expense.gst_treatment = gst_treatment
            expense.destination_of_supply = destination_of_supply
            expense.reverse_charge = reverse_charge
            expense.tax = tax
            expense.invoice = invoice
            expense.customer_name = customer
            expense.reporting_tags = reporting_tags
            expense.vendor = vendor
            expense.image=image
            expense.save()

            return redirect('expense_details',pk=expense.pk)
        else:
           
            c = addcustomer.objects.all()
            v = vendor_table.objects.all()
            accounts = Account.objects.all()
            account_types = set(Account.objects.values_list('type', flat=True))

            return render(request, 'editexpense.html', {'vendor': v, 'customer': c, 'accounts': accounts, 'account_types': account_types, 'expense': expense})

def dele(request,id):
    items=Expense.objects.filter(id=id)
    items.delete()
    
    return redirect('expensepage')
def vendor_dropdown(request):
    user = request.user

    options = []
    vendor_objects = vendor_table.objects.filter(user=user)
    for vendor in vendor_objects:
        vendor_data = {
            'id': vendor.id,
            'display_name': vendor.vendor_display_name,
            'company_name': vendor.company_name
        }
        options.append(vendor_data)

    return JsonResponse(options, safe=False)