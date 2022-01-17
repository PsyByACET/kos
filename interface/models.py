# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

## variable
GENDER = (
    ('M', 'мужской'),
    ("W", 'женский'),
)
CONTRACT_STATUS = (
    ("During","В процессе"),
    ("Completed","Завершен"),
    ("canceled","Отменён"),
)
TYPE_CLIENTS = (
    ('VIP', 'VIP'),
    ("PREMIUM", 'PREMIUM'),
    ("STANDARD", 'STANDARD'),
)
TYPE_HOTELS = (
    ('1', 'Однозвездочный'),
    ("2", 'Двухзвездочный'),
    ("3", 'Трёхзвездочный'),
    ("4", 'Четырёхзвездочный'),
    ("5", 'Пятизвездочный'),
)
AGENT = (
    ('yes','Да'),
    ('no','Нет'),
)
TYPE_NUMBERS = (
    ('STD', 'Стандартный'),
    ("BDR", 'Номер со спальней'),
    ("Superior", 'Большая стандартная'),
    ("Studio", 'Студия(с кухней)'),
    ("Family room", 'Семейная(больший размер)'),
    ('Family studio', 'Для семьи(из двух смежных комнат)'),
    ('Extra bed', 'Номер с одной большой кроватью'),
    ('Suit', 'Номер с гостинной и спальней'),
    ('De luxe', 'Двуместный однокомнатный номер(дорогая обстановка)'),
    ('Business', 'Большой номер с оргтехникой(ПК, факс)'),
    ('Honeymoon room', 'Номер для молодоженов'),
    ('Durplex', 'Двухэтажный номер'),
    ('Apartament', 'Номер приближенный к виду современной квартиры'),
    ('President', 'Самые раскошные номера(несколько спален, кабинет и тд.)'),
    ('Balcony', 'Номер с балконом'),
)


class City(models.Model):
    id_ciry = models.AutoField(primary_key=True)
    city_name = models.CharField(db_column='City name', max_length=65, blank=True, null=True, verbose_name="Город")  # Field name made lowercase. Field renamed to remove unsuitable characters.
    country_id_country = models.ForeignKey('Country', models.DO_NOTHING, db_column='Country_id_country')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'City'
    
    def __str__(self):
        return self.city_name


class Client(models.Model):
    id_client = models.AutoField(db_column='Id_client', primary_key=True)  # Field name made lowercase.
    name_client = models.CharField(db_column='Name_client', max_length=45, blank=False, null=True, verbose_name="ФИО")  # Field name made lowercase.
    status_client = models.CharField(db_column='Status_client', max_length=45, blank=False, null=True, choices=TYPE_CLIENTS, verbose_name="Статус")  # Field name made lowercase.
    

    class Meta:
        managed = False
        db_table = 'Client'
    
    def __str__(self):
        return self.name_client


class Contract(models.Model):
    id_contract = models.AutoField(primary_key=True)
    curency = models.CharField(db_column='Curency', max_length=25, blank=False, null=True, verbose_name="Стоимость")  # Field name made lowercase.
    contract_status = models.CharField(db_column='Contract_status', max_length=9, choices=CONTRACT_STATUS, verbose_name="Статус контракта")  # Field name made lowercase.
    start_trip = models.DateTimeField(db_column='Start_trip', blank=False, null=True, verbose_name="начало контракта")  # Field name made lowercase.
    end_trip = models.DateTimeField(db_column='End_trip', blank=False, null=True, verbose_name="Конец контракта")  # Field name made lowercase.
    agent = models.CharField(db_column='Agent', choices=AGENT, max_length=45, blank=True, null=True, verbose_name="Агент")  # Field name made lowercase.
    client_id_client = models.ForeignKey(Client, models.DO_NOTHING, db_column='Client_Id_client', verbose_name="Клиент")  # Field name made lowercase.
    employee_id_employee = models.ForeignKey('Employee', models.DO_NOTHING, db_column='Employee_Id_employee', verbose_name="Работник")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Contract'



class Country(models.Model):
    id_country = models.AutoField(primary_key=True)
    country_namel = models.CharField(db_column='Country namel', max_length=65, blank=True, null=True, verbose_name="Страна")  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Country'

    def __str__(self):
        return self.country_namel


class Currency(models.Model):
    id_currency = models.AutoField(db_column='Id_currency', primary_key=True)  # Field name made lowercase.
    currency_rate = models.FloatField(db_column='Currency_rate', blank=False, null=True, verbose_name="Курс")  # Field name made lowercase.
    currency_name = models.CharField(db_column='Currency_name', max_length=20, blank=False, null=True, verbose_name="Название валюты")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Currency'

    def __str__(self):
        return self.currency_name


class Deal(models.Model):
    id_deal = models.AutoField(db_column='Id_deal', primary_key=True)  # Field name made lowercase.
    status_deal = models.CharField(db_column='Status_deal', max_length=9,choices=CONTRACT_STATUS, blank=False, null=True, verbose_name="Статус сделки")  # Field name made lowercase.
    data = models.DateTimeField(db_column='Data', blank=False, null=True, verbose_name="Дата сделки")  # Field name made lowercase.
    sum_rub = models.FloatField(db_column='Sum_rub', blank=False, null=True, verbose_name="Сумма в рублях")  # Field name made lowercase.
    sum_currency = models.FloatField(db_column='Sum_currency', blank=False, null=True, verbose_name="Сумма в валюте")  # Field name made lowercase.
    id_currency = models.ForeignKey(Currency, models.DO_NOTHING, db_column='Id_currency', verbose_name="Валюта")  # Field name made lowercase.
    contract_id_contract = models.ForeignKey(Contract, models.DO_NOTHING, db_column='Contract_id_contract', verbose_name="Контракт")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Deal'



class Employee(models.Model):
    id_employee = models.AutoField(db_column='Id_employee', primary_key=True)  # Field name made lowercase.
    full_name = models.CharField(db_column='Full_name', max_length=80, blank=False, null=True, verbose_name="ФИО")  # Field name made lowercase.
    date_of_birth = models.DateField(db_column='Date_of_birth', blank=False, null=True, verbose_name="Дата рождения")  # Field name made lowercase.
    login = models.CharField(db_column='Login', unique=True, max_length=45, blank=True, null=True, verbose_name="Логин")  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255, blank=True, null=True, verbose_name="Пароль")  # Field name made lowercase.
    link_photo = models.ImageField(db_column='Link_photo', blank=True, null=True, verbose_name="ссылка на фото")  # Field name made lowercase.
    position_id_position = models.ForeignKey('Position', models.DO_NOTHING, db_column='Position_id_position', verbose_name="Должность")  # Field name made lowercase.
    office_id_office = models.ForeignKey('Office', models.DO_NOTHING, db_column='Office_id_office', verbose_name="Офис")  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Employee'

    def __str__(self):
        return self.full_name


class Hotel(models.Model):
    id_hotel = models.AutoField(primary_key=True)
    name_hotel = models.CharField(db_column='Name_hotel', max_length=45, blank=False, null=True, verbose_name="Название отеля")  # Field name made lowercase.
    category_hotel = models.CharField(db_column='Category_hotel',choices=TYPE_HOTELS, max_length=45, blank=False, null=True, verbose_name="Категория отеля")  # Field name made lowercase.
    adress_hotel = models.CharField(max_length=255, blank=False, null=False, verbose_name="Адрес отеля")

    class Meta:
        managed = False
        db_table = 'Hotel'

    def __str__(self):
        return self.name_hotel



class Office(models.Model):
    id_office = models.AutoField(primary_key=True)
    address_office = models.CharField(db_column='Address_office', max_length=255, blank=False, null=True, verbose_name="Адресс")  # Field name made lowercase.
    main = models.CharField(db_column='Main', max_length=6, blank=False, null=True, verbose_name="1-главный, 2-филиал")  # 1-main 2-branch
    office_name = models.CharField(db_column='office name', max_length=45, blank=False, null=True, verbose_name="Название")  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Office'
    
    def __str__(self):
        return self.office_name


class Passport(models.Model):
    id_passport = models.AutoField(db_column='Id_passport', primary_key=True)  # Field name made lowercase.
    date_of_birth = models.DateField(db_column='Date_of_Birth', blank=False, null=True, verbose_name="Дата рождения")  # Field name made lowercase.
    place_of_birth = models.CharField(db_column='Place_of_birth', max_length=45, blank=False, null=True, verbose_name="Место рождения")  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=1, choices=GENDER, verbose_name="Гендер")  # Field name made lowercase.
    serial_number_passport = models.PositiveIntegerField(db_column='Serial_number_passport', unique=True, blank=True, null=True, verbose_name="Серия и номер")  # Field name made lowercase.
    data_end_passport = models.DateField(db_column='Data_end_passport', blank=False, null=True, verbose_name="Окончание паспорта")  # Field name made lowercase.
    full_name = models.CharField(db_column='Full_name', max_length=80, blank=False, null=True, verbose_name="ФИО")  # Field name made lowercase.
    issued = models.CharField(db_column='Issued', max_length=45, blank=False, null=True, verbose_name="Кем выдан")  # Field name made lowercase.
    data_start_passport = models.DateField(db_column='Data_start_passport', blank=False, null=True, verbose_name="Дата начала паспорта")  # Field name made lowercase.
    client_id_client = models.OneToOneField(Client, models.DO_NOTHING, db_column='Client_Id_client')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Passport'


class Position(models.Model):
    id_position = models.AutoField(primary_key=True)
    name_position = models.CharField(db_column='Name_position', max_length=45, blank=False, null=True, verbose_name="Должность")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Position'

    def __str__(self):
        return self.name_position


class Room(models.Model):
    id_room = models.AutoField(primary_key=True)
    type_room = models.CharField(max_length=45, blank=False, null=True, choices=TYPE_NUMBERS, verbose_name="Тип комнаты")
    description_room = models.CharField(max_length=400, blank=False, null=True, verbose_name="Описание комнаты")
    hotel_id_hotel = models.ForeignKey(Hotel, models.DO_NOTHING, db_column='Hotel_id_hotel')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Room'


class Ticket(models.Model):
    id_tcket = models.AutoField(primary_key=True)
    trip_id_trip = models.ForeignKey('Trip', models.DO_NOTHING, db_column='Trip_id_trip', verbose_name="Поездка")  # Field name made lowercase.
    tourist_id_tourist = models.ForeignKey('Tourist', models.DO_NOTHING, db_column='Tourist_id_tourist', verbose_name="Турист")  # Field name made lowercase.
    nubmer_ticket = models.CharField(db_column='Nubmer ticket', max_length=45, blank=False, null=True, verbose_name="Номер билета")  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Ticket'

    def __str__(self):
        return self.nubmer_ticket


class Tourist(models.Model):
    id_tourist = models.AutoField(primary_key=True)
    contract_id_contract = models.ForeignKey(Contract, models.DO_NOTHING, db_column='Contract_id_contract', verbose_name="Контракт")  # Field name made lowercase.
    client_id_client = models.ForeignKey(Client, models.DO_NOTHING, db_column='Client_Id_client', verbose_name="Клиент")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tourist'

    def __str__(self):
        return self.client_id_client


class Trip(models.Model):
    id_trip = models.AutoField(primary_key=True)
    arrival_transport = models.CharField(db_column='Arrival_transport', max_length=45, blank=False, null=True, verbose_name="Транспорт прибытия")  # Field name made lowercase.
    exit_transport = models.CharField(db_column='Exit_transport', max_length=45, blank=False, null=True, verbose_name="Транспорт отбытия")  # Field name made lowercase.
    data_arrival = models.DateTimeField(db_column='Data_arrival', blank=False, null=True, verbose_name="Дата прибытия")  # Field name made lowercase.
    data_exit = models.DateTimeField(db_column='Data_exit', blank=False, null=True, verbose_name="Дата отъезда")  # Field name made lowercase.
    city_id_ciry = models.ForeignKey(City, models.DO_NOTHING, db_column='City_id_ciry', verbose_name="Город")  # Field name made lowercase.
    contract_id_contract = models.ForeignKey(Contract, models.DO_NOTHING, db_column='Contract_id_contract', verbose_name="Контракт")  # Field name made lowercase.
    hotel_id_hotel = models.ForeignKey(Hotel, models.DO_NOTHING, db_column='Hotel_id_hotel', verbose_name="Отель")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Trip'

    


class AdminInterfaceTheme(models.Model):
    name = models.CharField(unique=True, max_length=50)
    active = models.IntegerField()
    title = models.CharField(max_length=50)
    title_visible = models.IntegerField()
    logo = models.CharField(max_length=100)
    logo_visible = models.IntegerField()
    css_header_background_color = models.CharField(max_length=10)
    title_color = models.CharField(max_length=10)
    css_header_text_color = models.CharField(max_length=10)
    css_header_link_color = models.CharField(max_length=10)
    css_header_link_hover_color = models.CharField(max_length=10)
    css_module_background_color = models.CharField(max_length=10)
    css_module_text_color = models.CharField(max_length=10)
    css_module_link_color = models.CharField(max_length=10)
    css_module_link_hover_color = models.CharField(max_length=10)
    css_module_rounded_corners = models.IntegerField()
    css_generic_link_color = models.CharField(max_length=10)
    css_generic_link_hover_color = models.CharField(max_length=10)
    css_save_button_background_color = models.CharField(max_length=10)
    css_save_button_background_hover_color = models.CharField(max_length=10)
    css_save_button_text_color = models.CharField(max_length=10)
    css_delete_button_background_color = models.CharField(max_length=10)
    css_delete_button_background_hover_color = models.CharField(max_length=10)
    css_delete_button_text_color = models.CharField(max_length=10)
    list_filter_dropdown = models.IntegerField()
    related_modal_active = models.IntegerField()
    related_modal_background_color = models.CharField(max_length=10)
    related_modal_rounded_corners = models.IntegerField()
    logo_color = models.CharField(max_length=10)
    recent_actions_visible = models.IntegerField()
    favicon = models.CharField(max_length=100)
    related_modal_background_opacity = models.CharField(max_length=5)
    env_name = models.CharField(max_length=50)
    env_visible_in_header = models.IntegerField()
    env_color = models.CharField(max_length=10)
    env_visible_in_favicon = models.IntegerField()
    related_modal_close_button_visible = models.IntegerField()
    language_chooser_active = models.IntegerField()
    language_chooser_display = models.CharField(max_length=10)
    list_filter_sticky = models.IntegerField()
    form_pagination_sticky = models.IntegerField()
    form_submit_sticky = models.IntegerField()
    css_module_background_selected_color = models.CharField(max_length=10)
    css_module_link_selected_color = models.CharField(max_length=10)
    logo_max_height = models.PositiveSmallIntegerField()
    logo_max_width = models.PositiveSmallIntegerField()
    foldable_apps = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'admin_interface_theme'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Intermediatetransport(models.Model):
    id_transport = models.AutoField(primary_key=True)
    transport = models.CharField(db_column='Transport', max_length=45, blank=False, null=True, verbose_name="Транмпорт")  # Field name made lowercase.
    datatime_start = models.DateTimeField(db_column='DataTime_start', blank=False, null=True, verbose_name="Начало аренды")  # Field name made lowercase.
    datatime_end = models.DateTimeField(db_column='DataTime_end', blank=False, null=True, verbose_name="Конец аренды")  # Field name made lowercase.
    trip_id_trip = models.ForeignKey(Trip, models.DO_NOTHING, db_column='Trip_id_trip')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'intermediateTransport'