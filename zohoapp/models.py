from django.db import models
from django.contrib.auth.models import User

class company_details(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    contact_number = models.CharField(max_length=100,null=True,blank=True)
    company_name = models.CharField(max_length=100,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    pincode = models.IntegerField(null=True,blank=True)
    company_email = models.CharField(max_length=255,null=True,blank=True)
    business_name = models.CharField(max_length=255,null=True,blank=True)
    company_type = models.CharField(max_length=255,null=True,blank=True)
    industry_type = models.CharField(max_length=255,null=True,blank=True)
    profile_pic = models.ImageField(null=True,blank = True,upload_to = 'image/patient')




class Sales(models.Model):
    Account_type=models.TextField(max_length=255)
    Account_name=models.TextField(max_length=255)
    Acount_code=models.TextField(max_length=255)
    Account_desc=models.TextField(max_length=255)
    def __str__(self):
        return self.Account_name
    


class Purchase(models.Model):
    Account_type=models.TextField(max_length=255)
    Account_name=models.TextField(max_length=255)
    Acount_code=models.TextField(max_length=255)
    Account_desc=models.TextField(max_length=255)
    def __str__(self):
        return self.Account_name




class Unit(models.Model):
    unit=models.TextField(max_length=255)

    def __str__(self):
        return self.unit

    
    
    
class AddItem(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    type=models.TextField(max_length=255)
    Name=models.TextField(max_length=255)
    unit=models.ForeignKey(Unit,on_delete=models.CASCADE)
    sales=models.ForeignKey(Sales,on_delete=models.CASCADE)
    purchase=models.ForeignKey(Purchase,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    s_desc=models.TextField(max_length=255)
    p_desc=models.TextField(max_length=255)
    creat=models.CharField(max_length=255)
    s_price=models.CharField(max_length=255)
    p_price=models.TextField(max_length=255)
    satus=models.TextField(default='active')
    interstate=models.CharField(max_length=255)
    intrastate=models.CharField(max_length=255)

class History(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True)
    message=models.CharField(max_length=255)
    p=models.ForeignKey(AddItem,on_delete=models.CASCADE)
class Account(models.Model):
    name=models.CharField(max_length=255)
    pname=models.CharField(max_length=255)
    code=models.CharField(max_length=255)
    type=models.CharField(max_length=255)
    description=models.TextField(blank=True)
class payment_terms(models.Model):
    Terms=models.CharField(max_length=100,null=True,blank=True)
    Days=models.IntegerField(null=True,blank=True)  
class addcustomer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer_name= models.CharField(max_length=100,null=True,blank=True)
    customerType= models.CharField(max_length=100,null=True,blank=True)
    companyName= models.CharField(max_length=100,null=True,blank=True)
    customerEmail= models.CharField(max_length=100,null=True,blank=True)
    customerWorkPhone= models.CharField(max_length=100,null=True,blank=True)
    customerMobile= models.CharField(max_length=100,null=True,blank=True)
    skype=models.CharField(max_length=100,null=True,blank=True)
    designation=models.CharField(max_length=100,null=True,blank=True)
    department=models.CharField(max_length=100,null=True,blank=True)
    website=models.CharField(max_length=100,null=True,blank=True)
    GSTTreatment=models.CharField(max_length=100,null=True,blank=True)
    placeofsupply=models.CharField(max_length=100,null=True,blank=True)
    Taxpreference=models.CharField(max_length=100,null=True,blank=True)
    currency=models.CharField(max_length=100,null=True,blank=True)
    OpeningBalance= models.IntegerField(null=True,blank=True)
    PaymentTerms=models.CharField(max_length=100,null=True,blank=True)
    PriceList=models.CharField(max_length=100,null=True,blank=True)

    PortalLanguage=models.CharField(max_length=100,null=True,blank=True)
    Facebook=models.CharField(max_length=100,null=True,blank=True)
    Twitter=models.CharField(max_length=100,null=True,blank=True)
    Attention=models.CharField(max_length=100,null=True,blank=True)
    country=models.CharField(max_length=100,null=True,blank=True)
    Address1=models.CharField(max_length=100,null=True,blank=True)
    Address2=models.CharField(max_length=100,null=True,blank=True)
    city=models.CharField(max_length=100,null=True,blank=True)
    state=models.CharField(max_length=100,null=True,blank=True)
    zipcode=models.CharField(max_length=100,null=True,blank=True)
    phone1=models.CharField(max_length=100,null=True,blank=True)
    fax=models.CharField(max_length=100,null=True,blank=True)

    CPsalutation=models.CharField(max_length=100,null=True,blank=True)
    Firstname=models.CharField(max_length=100,null=True,blank=True)
    Lastname=models.CharField(max_length=100,null=True,blank=True)
    CPemail=models.CharField(max_length=100,null=True,blank=True)#
    CPphone=models.CharField(max_length=100,null=True,blank=True)
    CPmobile=models.CharField(max_length=100,null=True,blank=True)
    CPskype=models.CharField(max_length=100,null=True,blank=True)
    CPdesignation=models.CharField(max_length=100,null=True,blank=True)
    CPdepartment=models.CharField(max_length=100,null=True,blank=True)

class vendor_table(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    salutation=models.CharField(max_length=25)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    company_name=models.CharField(max_length=150)
    vendor_display_name=models.CharField(max_length=150)
    vendor_email=models.CharField(max_length=250)
    vendor_wphone=models.CharField(max_length=50)
    vendor_mphone=models.CharField(max_length=50)
    skype_number=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    website=models.CharField(max_length=250)
    gst_treatment=models.CharField(max_length=100)
    gst_number=models.CharField(max_length=50,null=True)
    pan_number=models.CharField(max_length=50,null=True)
    source_supply=models.CharField(max_length=100)
    currency=models.CharField(max_length=50)
    opening_bal=models.CharField(max_length=100)
    payment_terms=models.CharField(max_length=100)
    battention=models.CharField(max_length=100,default='')
    bcountry=models.CharField(max_length=100,default='')
    baddress=models.CharField(max_length=300,default='')
    bcity=models.CharField(max_length=100,default='')
    bstate=models.CharField(max_length=100,default='')
    bzip=models.CharField(max_length=100,default='')
    bphone=models.CharField(max_length=100,default='')
    bfax=models.CharField(max_length=100,default='')
    sattention=models.CharField(max_length=100,default='')
    scountry=models.CharField(max_length=100,default='')
    saddress=models.CharField(max_length=300,default='')
    scity=models.CharField(max_length=100,default='')
    sstate=models.CharField(max_length=100,default='')
    szip=models.CharField(max_length=100,default='')
    sphone=models.CharField(max_length=100,default='')
    sfax=models.CharField(max_length=100,default='')



class contact_person_table(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    vendor=models.ForeignKey(vendor_table,on_delete=models.CASCADE,null=True)
    salutation=models.CharField(max_length=25)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=200)
    work_phone=models.CharField(max_length=50)
    mobile=models.CharField(max_length=50)
    skype_number=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    department=models.CharField(max_length=50)

class remarks_table(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    vendor=models.ForeignKey(vendor_table,on_delete=models.CASCADE,null=True)
    remarks=models.CharField(max_length=500)

class Expense(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    expense_account=models.ForeignKey(Account,on_delete=models.CASCADE)
    amount=models.TextField(max_length=255)
    currency=models.TextField(max_length=255)
    expense_type=models.TextField(max_length=255)
    paid=models.TextField(max_length=255)
    vendor= models.ForeignKey(vendor_table, on_delete=models.CASCADE)
    notes=models.TextField(max_length=255)
    hsn_code=models.TextField(max_length=255)
    gst_treatment =models.TextField(max_length=255)
    destination_of_supply=models.TextField(max_length=255)
    reverse_charge=models.TextField(max_length=255)
    tax=models.TextField(max_length=255)
    invoice=models.TextField(max_length=255)
    # customer_name=models.ForeignKey(addcustomer,on_delete=models.CASCADE)
    customer_name = models.ForeignKey(addcustomer, on_delete=models.CASCADE)
    reporting_tags=models.TextField(max_length=255,null=True, blank=True)
    date = models.DateField()
    sac=models.TextField(max_length=255)
    taxamt=models.TextField(max_length=255)
    # attachment = models.FileField(upload_to='expense_attachments/', blank=True, null=True)
class Attach(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default='')
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, null=True)
    attachment= models.FileField(upload_to='attachment/', blank=True, null=True)



