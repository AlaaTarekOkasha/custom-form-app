from django.conf import settings
from django.db import models

# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class ExtraInfo(models.Model):
    """
    This model contains two extra fields that will be saved when a user registers.
    The form that wraps this model is in the forms.py file.
    """
    user = models.OneToOneField(USER_MODEL, null=True,  related_name='user+', on_delete=models.CASCADE)
    
    COUNTRIES  = (
                ('AF' , 'Afghanistan' ),
                ('AX' , 'Åland Islands' ),
                ('AL' , 'Albania' ),
                ('DZ' , 'Algeria' ),
                ('AS' , 'American Samoa' ),
                ('AD' , 'Andorra' ),
                ('AO' , 'Angola' ),
                ('AI' , 'Anguilla' ),
                ('AQ' , 'Antarctica' ),
                ('AG' , 'Antigua and Barbuda' ),
                ('AR' , 'Argentina' ),
                ('AM' , 'Armenia' ),
                ('AW' , 'Aruba' ),
                ('AU' , 'Australia' ),
                ('AT' , 'Austria' ),
                ('AZ' , 'Azerbaijan' ),
                ('BS' , 'Bahamas' ),
                ('BH' , 'Bahrain' ),
                ('BD' , 'Bangladesh' ),
                ('BB' , 'Barbados' ),
                ('BY' , 'Belarus' ),
                ('BE' , 'Belgium' ),
                ('BZ' , 'Belize' ),
                ('BJ' , 'Benin' ),
                ('BM' , 'Bermuda' ),
                ('BT' , 'Bhutan' ),
                ('BO' , 'Bolivia' ),
                ('BA' , 'Bosnia and Herzegovina' ),
                ('BW' , 'Botswana' ),
                ('BV' , 'Bouvet Island' ),
                ('BR' , 'Brazil' ),
                ('IO' , 'British Indian Ocean Territory' ),
                ('BN' , 'Brunei Darussalam' ),
                ('BG' , 'Bulgaria' ),
                ('BF' , 'Burkina Faso' ),
                ('BI' , 'Burundi' ),
                ('KH' , 'Cambodia' ),
                ('CM' , 'Cameroon' ),
                ('CA' , 'Canada' ),
                ('CV' , 'Cape Verde' ),
                ('KY' , 'Cayman Islands' ),
                ('CF' , 'Central African Republic' ),
                ('TD' , 'Chad' ),
                ('CL' , 'Chile' ),
                ('CN' , 'China' ),
                ('CX' , 'Christmas Island' ),
                ('CC' , 'Cocos  Islands' ),
                ('CO' , 'Colombia' ),
                ('KM' , 'Comoros' ),
                ('CG' , 'Congo' ),
                ('CD' , 'Congo The Democratic Republic of The' ),
                ('CK' , 'Cook Islands' ),
                ('CR' , 'Costa Rica' ),
                ('CI' , 'Cote D ivoire' ),
                ('HR' , 'Croatia' ),
                ('CU' , 'Cuba' ),
                ('CY' , 'Cyprus' ),
                ('CZ' , 'Czechia' ),
                ('DK' , 'Denmark' ),
                ('DJ' , 'Djibouti' ),
                ('DM' , 'Dominica' ),
                ('DO' , 'Dominican Republic' ),
                ('EC' , 'Ecuador' ),
                ('EG' , 'Egypt' ),
                ('SV' , 'El Salvador' ),
                ('GQ' , 'Equatorial Guinea' ),
                ('ER' , 'Eritrea' ),
                ('EE' , 'Estonia' ),
                ('ET' , 'Ethiopia' ),
                ('FK' , 'Falkland Islands' ),
                ('FO' , 'Faroe Islands' ),
                ('FJ' , 'Fiji' ),
                ('FI' , 'Finland' ),
                ('FR' , 'France' ),
                ('GF' , 'French Guiana' ),
                ('PF' , 'French Polynesia' ),
                ('TF' , 'French Southern Territories' ),
                ('GA' , 'Gabon' ),
                ('GM' , 'Gambia' ),
                ('GE' , 'Georgia' ),
                ('DE' , 'Germany' ),
                ('GH' , 'Ghana' ),
                ('GI' , 'Gibraltar' ),
                ('GR' , 'Greece' ),
                ('GL' , 'Greenland' ),
                ('GD' , 'Grenada' ),
                ('GP' , 'Guadeloupe' ),
                ('GU' , 'Guam' ),
                ('GT' , 'Guatemala' ),
                ('GG' , 'Guernsey' ),
                ('GN' , 'Guinea' ),
                ('GW' , 'Guinea-bissau' ),
                ('GY' , 'Guyana' ),
                ('HT' , 'Haiti' ),
                ('HM' , 'Heard Island and Mcdonald Islands' ),
                ('VA' , 'Vatican City State' ),
                ('HN' , 'Honduras' ),
                ('HK' , 'Hong Kong' ),
                ('HU' , 'Hungary' ),
                ('IS' , 'Iceland' ),
                ('IN' , 'India' ),
                ('ID' , 'Indonesia' ),
                ('IR' , 'Iran Islamic Republic of' ),
                ('IQ' , 'Iraq' ),
                ('IE' , 'Ireland' ),
                ('IM' , 'Isle of Man' ),
                ('IL' , 'Israel' ),
                ('IT' , 'Italy' ),
                ('JM' , 'Jamaica' ),
                ('JP' , 'Japan' ),
                ('JE' , 'Jersey' ),
                ('JO' , 'Jordan' ),
                ('KZ' , 'Kazakhstan' ),
                ('KE' , 'Kenya' ),
                ('KI' , 'Kiribati' ),
                ('KP' , 'Korea Democratic Peoples Republic of' ),
                ('KR' , 'Korea Republic of' ),
                ('KW' , 'Kuwait' ),
                ('KG' , 'Kyrgyzstan' ),
                ('LA' , 'Laos People Democratic Republic' ),
                ('LV' , 'Latvia' ),
                ('LB' , 'Lebanon' ),
                ('LS' , 'Lesotho' ),
                ('LR' , 'Liberia' ),
                ('LY' , 'Libyan Arab Jamahiriya' ),
                ('LI' , 'Liechtenstein' ),
                ('LT' , 'Lithuania' ),
                ('LU' , 'Luxembourg' ),
                ('MO' , 'Macao' ),
                ('MK' , 'Macedonia The Former Yugoslav Republic of' ),
                ('MG' , 'Madagascar' ),
                ('MW' , 'Malawi' ),
                ('MY' , 'Malaysia' ),
                ('MV' , 'Maldives' ),
                ('ML' , 'Mali' ),
                ('MT' , 'Malta' ),
                ('MH' , 'Marshall Islands' ),
                ('MQ' , 'Martinique' ),
                ('MR' , 'Mauritania' ),
                ('MU' , 'Mauritius' ),
                ('YT' , 'Mayotte' ),
                ('MX' , 'Mexico' ),
                ('FM' , 'Micronesia' ),
                ('MD' , 'Moldova' ),
                ('MC' , 'Monaco' ),
                ('MN' , 'Mongolia' ),
                ('ME' , 'Montenegro' ),
                ('MS' , 'Montserrat' ),
                ('MA' , 'Morocco' ),
                ('MZ' , 'Mozambique' ),
                ('MM' , 'Myanmar' ),
                ('NA' , 'Namibia' ),
                ('NR' , 'Nauru' ),
                ('NP' , 'Nepal' ),
                ('NL' , 'Netherlands' ),
                ('AN' , 'Netherlands Antilles' ),
                ('NC' , 'New Caledonia' ),
                ('NZ' , 'New Zealand' ),
                ('NI' , 'Nicaragua' ),
                ('NE' , 'Niger' ),
                ('NG' , 'Nigeria' ),
                ('NU' , 'Niue' ),
                ('NF' , 'Norfolk Island' ),
                ('MP' , 'Northern Mariana Islands' ),
                ('NO' , 'Norway' ),
                ('OM' , 'Oman' ),
                ('PK' , 'Pakistan' ),
                ('PW' , 'Palau' ),
                ('PS' , 'Palestinian Territory Occupied' ),
                ('PA' , 'Panama' ),
                ('PG' , 'Papua New Guinea' ),
                ('PY' , 'Paraguay' ),
                ('PE' , 'Peru' ),
                ('PH' , 'Philippines' ),
                ('PN' , 'Pitcairn' ),
                ('PL' , 'Poland' ),
                ('PT' , 'Portugal' ),
                ('PR' , 'Puerto Rico' ),
                ('QA' , 'Qatar' ),
                ('RE' , 'Reunion' ),
                ('RO' , 'Romania' ),
                ('RU' , 'Russian Federation' ),
                ('RW' , 'Rwanda' ),
                ('SH' , 'Saint Helena' ),
                ('KN' , 'Saint Kitts and Nevis' ),
                ('LC' , 'Saint Lucia' ),
                ('PM' , 'Saint Pierre and Miquelon' ),
                ('VC' , 'Saint Vincent and The Grenadines' ),
                ('WS' , 'Samoa' ),
                ('SM' , 'San Marino' ),
                ('ST' , 'Sao Tome and Principe' ),
                ('SA' , 'Saudi Arabia' ),
                ('SN' , 'Senegal' ),
                ('RS' , 'Serbia' ),
                ('SC' , 'Seychelles' ),
                ('SL' , 'Sierra Leone' ),
                ('SG' , 'Singapore' ),
                ('SK' , 'Slovakia' ),
                ('SI' , 'Slovenia' ),
                ('SB' , 'Solomon Islands' ),
                ('SO' , 'Somalia' ),
                ('ZA' , 'South Africa' ),
                ('GS' , 'South Georgia and The South Sandwich Islands' ),
                ('ES' , 'Spain' ),
                ('LK' , 'Sri Lanka' ),
                ('SD' , 'Sudan' ),
                ('SR' , 'Suriname' ),
                ('SJ' , 'Svalbard and Jan Mayen' ),
                ('SZ' , 'Swaziland' ),
                ('SE' , 'Sweden' ),
                ('CH' , 'Switzerland' ),
                ('SY' , 'Syrian Arab Republic' ),
                ('TW' , 'Taiwan Province of China' ),
                ('TJ' , 'Tajikistan' ),
                ('TZ' , 'Tanzania United Republic of' ),
                ('TH' , 'Thailand' ),
                ('TL' , 'Timor-leste' ),
                ('TG' , 'Togo' ),
                ('TK' , 'Tokelau' ),
                ('TO' , 'Tonga' ),
                ('TT' , 'Trinidad and Tobago' ),
                ('TN' , 'Tunisia' ),
                ('TR' , 'Turkey' ),
                ('TM' , 'Turkmenistan' ),
                ('TC' , 'Turks and Caicos Islands' ),
                ('TV' , 'Tuvalu' ),
                ('UG' , 'Uganda' ),
                ('UA' , 'Ukraine' ),
                ('AE' , 'United Arab Emirates' ),
                ('GB' , 'United Kingdom' ),
                ('US' , 'United States' ),
                ('UM' , 'United States Minor Outlying Islands' ),
                ('UY' , 'Uruguay' ),
                ('UZ' , 'Uzbekistan' ),
                ('VU' , 'Vanuatu' ),
                ('VE' , 'Venezuela' ),
                ('VN' , 'Viet Nam' ),
                ('VG' , 'Virgin Islands British' ),
                ('VI' , 'Virgin Islands US' ),
                ('WF' , 'Wallis and Futuna' ),
                ('EH' , 'Western Sahara' ),
                ('YE' , 'Yemen' ),
                ('ZM' , 'Zambia' ),
                ('ZW' , 'Zimbabwe'), 
                )
    
    phone_codes = (
                ('297', 'Aruba'),
                ('93', 'fghanistan'),
                ('244', 'Angola'),
                ('1264', 'Anguilla'),
                ('358', 'Aland Islands'),
                ('355', 'Albania'),
                ('376', 'Andorra'),
                ('971', 'United Arab Emirates'),
                ('54', 'Argentina'),
                ('374', 'Armenia'),
                ('1684', 'American Samoa'),
                ('1268', 'Antigua and Barbuda'),
                ('61', 'Australia'),
                ('43', 'Austria'),
                ('994', 'Azerbaijan'),
                ('257', 'Burundi'),
                ('32', 'Belgium'),
                ('229', 'Benin'),
                ('226', 'Burkina Faso'),
                ('880', 'Bangladesh'),
                ('359', 'Bulgaria'),
                ('973', 'Bahrain'),
                ('1242', 'Bahamas'),
                ('387', 'Bosnia and Herzegovina'),
                ('590', 'Saint Barthelemy'),
                ('375', 'Belarus'),
                ('501', 'Belize'),
                ('1441', 'Bermuda'),
                ('591', 'Bolivia'),
                ('55', 'Brazil'),
                ('1246', 'Barbados'),
                ('673', 'Brunei'),
                ('975', 'Bhutan'),
                ('267', 'Botswana'),
                ('236', 'Central African Republic'),
                ('1', 'Canada'),
                ('61', 'Cocos (Keeling) Islands'),
                ('41', 'Switzerland'),
                ('56', 'Chile'),
                ('86', 'China'),
                ('225', 'Ivory Coast'),
                ('237', 'Cameroon'),
                ('243', 'DR Congo'),
                ('242', 'Republic of the Congo'),
                ('682', 'Cook Islands'),
                ('57', 'Colombia'),
                ('269', 'Comoros'),
                ('238', 'ape Verde'),
                ('506', 'Costa Rica'),
                ('53', 'Cuba'),
                ('5999', 'Curaçao'),
                ('61', 'Christmas Island'),
                ('1345', 'Cayman Islands'),
                ('357', 'Cyprus'),
                ('420', 'Czech Republic'),
                ('49', 'Germany'),
                ('253', 'Djibouti'),
                ('1767', 'Dominica'),
                ('45', 'Denmark'),
                ('1809', 'Dominican Republic'),
                ('1829', 'Dominican Republic'),
                ('1849', 'Dominican Republic'),
                ('213', 'Algeria'),
                ('593', 'Ecuador'),
                ('20', 'Egypt'),
                ('291', 'Eritrea'),
                ('212', 'Western Sahara'),
                ('34', 'Spain'),
                ('372', 'Estonia'),
                ('251', 'Ethiopia'),
                ('358', 'Finland'),
                ('679', 'Fiji'),
                ('500', 'Falkland Islands'),
                ('33', 'France'),
                ('298', 'Faroe Islands'),
                ('691', 'Micronesia'),
                ('241', 'Gabon'),
                ('44', 'United Kingdom'),
                ('995', 'Georgia'),
                ('44', 'Guernsey'),
                ('233', 'Ghana'),
                ('350', 'Gibraltar'),
                ('224', 'Guinea'),
                ('590', 'Guadeloupe'),
                ('220', 'Gambia'),
                ('245', 'Guinea-Bissau'),
                ('240', 'Equatorial Guinea'),
                ('30', 'Greece'),
                ('1473', 'Grenada'),
                ('299', 'Greenland'),
                ('502', 'Guatemala'),
                ('594', 'French Guiana'),
                ('1671', 'Guam'),
                ('592', 'Guyana'),
                ('852', 'Hong Kong'),
                ('504', 'Honduras'),
                ('385', 'Croatia'),
                ('509', 'Haiti'),
                ('36', 'Hungary'),
                ('62', 'Indonesia'),
                ('44', 'Isle of Man'),
                ('91', 'India'),
                ('246', 'British Indian Ocean Territory'),
                ('353', 'Ireland'),
                ('98', 'Iran'),
                ('964', 'Iraq'),
                ('354', 'Iceland'),
                ('972', 'Israel'),
                ('39', 'Italy'),
                ('1876', 'Jamaica'),
                ('44', 'Jersey'),
                ('962', 'Jordan'),
                ('81', 'Japan'),
                ('76', 'Kazakhstan'),
                ('77', 'Kazakhstan'),
                ('254', 'Kenya'),
                ('996', 'Kyrgyzstan'),
                ('855', 'Cambodia'),
                ('686', 'Kiribati'),
                ('1869', 'Saint Kitts and Nevis'),
                ('82', 'South Korea'),
                ('383', 'Kosovo'),
                ('965', 'Kuwait'),
                ('856', 'Laos'),
                ('961', 'Lebanon'),
                ('231', 'Liberia'),
                ('218', 'Libya'),
                ('1758', 'Saint Lucia'),
                ('423', 'Liechtenstein'),
                ('94', 'Sri Lanka'),
                ('266', 'Lesotho'),
                ('370', 'Lithuania'),
                ('352', 'Luxembourg'),
                ('371', 'Latvia'),
                ('853', 'Macau'),
                ('590', 'Saint Martin'),
                ('212', 'Morocco'),
                ('377', 'Monaco'),
                ('373', 'Moldova'),
                ('261', 'Madagascar'),
                ('960', 'Maldives'),
                ('52', 'Mexico'),
                ('692', 'Marshall Islands'),
                ('389', 'Macedonia'),
                ('223', 'Mali'),
                ('356', 'Malta'),
                ('95', 'Myanmar'),
                ('382', 'Montenegro'),
                ('976', 'Mongolia'),
                ('1670', 'Northern Mariana Islands'),
                ('258', 'Mozambique'),
                ('222', 'Mauritania'),
                ('1664', 'Montserrat'),
                ('596', 'Martinique'),
                ('230', 'Mauritius'),
                ('265', 'Malawi'),
                ('60', 'Malaysia'),
                ('262', 'Mayotte'),
                ('264', 'Namibia'),
                ('687', 'New Caledonia'),
                ('227', 'Niger'),
                ('672', 'Norfolk Island'),
                ('234', 'Nigeria'),
                ('505', 'Nicaragua'),
                ('683', 'Niue'),
                ('31', 'Netherlands'),
                ('47', 'Norway'),
                ('977', 'Nepal'),
                ('674', 'Nauru'),
                ('64', 'New Zealand'),
                ('968', 'Oman'),
                ('92', 'Pakistan'),
                ('507', 'Panama'),
                ('64', 'Pitcairn Islands'),
                ('51', 'Peru'),
                ('63', 'Philippines'),
                ('680', 'Palau'),
                ('675', 'Papua New Guinea'),
                ('48', 'Poland'),
                ('1787', 'Puerto Rico'),
                ('1939', 'Puerto Rico'),
                ('850', 'North Korea'),
                ('351', 'Portugal'),
                ('595', 'Paraguay'),
                ('970', 'Palestine'),
                ('689', 'French Polynesia'),
                ('974', 'Qatar'),
                ('262', 'Reunion'),
                ('40', 'Romania'),
                ('7', 'Russia'),
                ('250', 'Rwanda'),
                ('966', 'Saudi Arabia'),
                ('249', 'Sudan'),
                ('221', 'Senegal'),
                ('65', 'Singapore'),
                ('500', 'South Georgia'),
                ('4779', 'Svalbard and Jan Mayen'),
                ('677', 'Solomon Islands'),
                ('232', 'Sierra Leone'),
                ('503', 'El Salvador'),
                ('378', 'San Marino'),
                ('252', 'Somalia'),
                ('508', 'Saint Pierre and Miquelon'),
                ('381', 'Serbia'),
                ('211', 'South Sudan'),
                ('239', 'Sao Tome and Principe'),
                ('597', 'Suriname'),
                ('421', 'Slovakia'),
                ('386', 'Slovenia'),
                ('46', 'Sweden'),
                ('268', 'Swaziland'),
                ('1721', 'Sint Maarten'),
                ('248', 'Seychelles'),
                ('963', 'Syria'),
                ('1649', 'Turks and Caicos Islands'),
                ('235', 'Chad'),
                ('228', 'Togo'),
                ('66', 'Thailand'),
                ('992', 'Tajikistan'),
                ('690', 'Tokelau'),
                ('993', 'Turkmenistan'),
                ('670', 'Timor-Leste'),
                ('676', 'Tonga'),
                ('1868', 'Trinidad and Tobago'),
                ('216', 'Tunisia'),
                ('90', 'Turkey'),
                ('688', 'Tuvalu'),
                ('886', 'Taiwan'),
                ('255', 'Tanzania'),
                ('256', 'Uganda'),
                ('380', 'Ukraine'),
                ('598', 'Uruguay'),
                ('1', 'United States'),
                ('998', 'Uzbekistan'),
                ('3906698', 'Vatican City'),
                ('379', 'Vatican City'),
                ('1784', 'Saint Vincent and the Grenadines'),
                ('58', 'Venezuela'),
                ('1284', 'British Virgin Islands'),
                ('1340', 'United States Virgin Islands'),
                ('84', 'Vietnam'),
                ('678', 'Vanuatu'),
                ('681', 'Wallis and Futuna'),
                ('685', 'Samoa'),
                ('967', 'Yemen'),
                ('27', 'South Africa'),
                ('260', 'Zambia'),
                ('263', 'Zimbabwe')
                )

    DAYS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('17', '18'),
        ('19', '19'),
        ('20', '20'),
        ('21', '21'),
        ('22', '22'),
        ('23', '23'),
        ('24', '24'),
        ('25', '25'),
        ('26', '26'),
        ('27', '27'),
        ('28', '28'),
        ('29', '29'),
        ('30', '30'),
        ('31', '31')                                        
    )
    
    MONTHS = (
        ('01', 'January'),
        ('02', 'February'),
        ('03', 'March'),
        ('04', 'April'),
        ('05', 'May'),
        ('06', 'June'),
        ('07', 'July'),
        ('08', 'August'),
        ('09', 'September'),
        ('10', 'October'),
        ('11', 'November'),
        ('12', 'December')        
    )
    
    day_of_birth = models.CharField(
        verbose_name="Day",
        choices=DAYS,
        blank=True,
        max_length=100,
    )
    
    month_of_birth = models.CharField(
    verbose_name="Month",
    choices=MONTHS,
    blank=True,
    max_length=100,
    )
    
    country_of_origin = models.CharField(
        verbose_name="Country of Origin",
        choices=COUNTRIES,
        blank=True,
        max_length=100,
    )
    
    country_codes = models.CharField(
        verbose_name="Country Code",
        choices=phone_codes,
        blank=True,
        max_length=100,
    )
        
    phone_number = models.CharField(
        verbose_name="Phone Number",
        max_length=100,
    )    
    
    
    def __str__(self):
        result = '{0.user} {0.day_of_birth} {0.month_of_birth} {0.country_of_origin} {0.country_codes} {0.phone_number}' #{0.date_of_birth} 
        return result.format(self)
