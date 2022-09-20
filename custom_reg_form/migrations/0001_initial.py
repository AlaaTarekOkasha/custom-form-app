
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_birth', models.CharField(verbose_name="Day", max_length=100,
                 choices = [
                    
                    (b'1', b'1'),
                    (b'2', b'2'),
                    (b'3', b'3'),
                    (b'4', b'4'),
                    (b'5', b'5'),
                    (b'6', b'6'),
                    (b'7', b'7'),
                    (b'8', b'8'),
                    (b'9', b'9'),
                    (b'10', b'10'),
                    (b'11', b'11'),
                    (b'12', b'12'),
                    (b'13', b'13'),
                    (b'14', b'14'),
                    (b'15', b'15'),
                    (b'16', b'16'),
                    (b'17', b'17'),
                    (b'17', b'18'),
                    (b'19', b'19'),
                    (b'20', b'20'),
                    (b'21', b'21'),
                    (b'22', b'22'),
                    (b'23', b'23'),
                    (b'24', b'24'),
                    (b'25', b'25'),
                    (b'26', b'26'),
                    (b'27', b'27'),
                    (b'28', b'28'),
                    (b'29', b'29'),
                    (b'30', b'30'),
                    (b'31', b'31') ] )),
                ('month_of_birth', models.CharField(verbose_name="Month", max_length=100,
                 choices = [
                    
                    (b'01', b'January'),
                    (b'02', b'February'),
                    (b'03', b'March'),
                    (b'04', b'April'),
                    (b'05', b'May'),
                    (b'06', b'June'),
                    (b'07', b'July'),
                    (b'08', b'August'),
                    (b'09', b'September'),
                    (b'10', b'October'),
                    (b'11', b'November'),
                    (b'12', b'December')  ] )),               
                ('country_of_origin', models.CharField(verbose_name="Country of Origin", max_length=100,
                 choices = [

                    (b'AF' , b'Afghanistan' ),
                    (b'AX' , b'Aland Islands' ),
                    (b'AL' , b'Albania' ),
                    (b'DZ' , b'Algeria' ),
                    (b'AS' , b'American Samoa' ),
                    (b'AD' , b'Andorra' ),
                    (b'AO' , b'Angola' ),
                    (b'AI' , b'Anguilla' ),
                    (b'AQ' , b'Antarctica' ),
                    (b'AG' , b'Antigua and Barbuda' ),
                    (b'AR' , b'Argentina' ),
                    (b'AM' , b'Armenia' ),
                    (b'AW' , b'Aruba' ),
                    (b'AU' , b'Australia' ),
                    (b'AT' , b'Austria' ),
                    (b'AZ' , b'Azerbaijan' ),
                    (b'BS' , b'Bahamas' ),
                    (b'BH' , b'Bahrain' ),
                    (b'BD' , b'Bangladesh' ),
                    (b'BB' , b'Barbados' ),
                    (b'BY' , b'Belarus' ),
                    (b'BE' , b'Belgium' ),
                    (b'BZ' , b'Belize' ),
                    (b'BJ' , b'Benin' ),
                    (b'BM' , b'Bermuda' ),
                    (b'BT' , b'Bhutan' ),
                    (b'BO' , b'Bolivia' ),
                    (b'BA' , b'Bosnia and Herzegovina' ),
                    (b'BW' , b'Botswana' ),
                    (b'BV' , b'Bouvet Island' ),
                    (b'BR' , b'Brazil' ),
                    (b'IO' , b'British Indian Ocean Territory' ),
                    (b'BN' , b'Brunei Darussalam' ),
                    (b'BG' , b'Bulgaria' ),
                    (b'BF' , b'Burkina Faso' ),
                    (b'BI' , b'Burundi' ),
                    (b'KH' , b'Cambodia' ),
                    (b'CM' , b'Cameroon' ),
                    (b'CA' , b'Canada' ),
                    (b'CV' , b'Cape Verde' ),
                    (b'KY' , b'Cayman Islands' ),
                    (b'CF' , b'Central African Republic' ),
                    (b'TD' , b'Chad' ),
                    (b'CL' , b'Chile' ),
                    (b'CN' , b'China' ),
                    (b'CX' , b'Christmas Island' ),
                    (b'CC' , b'Cocos Keeling Islands' ),
                    (b'CO' , b'Colombia' ),
                    (b'KM' , b'Comoros' ),
                    (b'CG' , b'Congo' ),
                    (b'CD' , b'Congo, The Democratic Republic of The' ),
                    (b'CK' , b'Cook Islands' ),
                    (b'CR' , b'Costa Rica' ),
                    (b'CI' , b'Cote D ivoire' ),
                    (b'HR' , b'Croatia' ),
                    (b'CU' , b'Cuba' ),
                    (b'CY' , b'Cyprus' ),
                    (b'CZ' , b'Czechia' ),
                    (b'DK' , b'Denmark' ),
                    (b'DJ' , b'Djibouti' ),
                    (b'DM' , b'Dominica' ),
                    (b'DO' , b'Dominican Republic' ),
                    (b'EC' , b'Ecuador' ),
                    (b'EG' , b'Egypt' ),
                    (b'SV' , b'El Salvador' ),
                    (b'GQ' , b'Equatorial Guinea' ),
                    (b'ER' , b'Eritrea' ),
                    (b'EE' , b'Estonia' ),
                    (b'ET' , b'Ethiopia' ),
                    (b'FK' , b'Falkland Islands' ),
                    (b'FO' , b'Faroe Islands' ),
                    (b'FJ' , b'Fiji' ),
                    (b'FI' , b'Finland' ),
                    (b'FR' , b'France' ),
                    (b'GF' , b'French Guiana' ),
                    (b'PF' , b'French Polynesia' ),
                    (b'TF' , b'French Southern Territories' ),
                    (b'GA' , b'Gabon' ),
                    (b'GM' , b'Gambia' ),
                    (b'GE' , b'Georgia' ),
                    (b'DE' , b'Germany' ),
                    (b'GH' , b'Ghana' ),
                    (b'GI' , b'Gibraltar' ),
                    (b'GR' , b'Greece' ),
                    (b'GL' , b'Greenland' ),
                    (b'GD' , b'Grenada' ),
                    (b'GP' , b'Guadeloupe' ),
                    (b'GU' , b'Guam' ),
                    (b'GT' , b'Guatemala' ),
                    (b'GG' , b'Guernsey' ),
                    (b'GN' , b'Guinea' ),
                    (b'GW' , b'Guinea-bissau' ),
                    (b'GY' , b'Guyana' ),
                    (b'HT' , b'Haiti' ),
                    (b'HM' , b'Heard Island and Mcdonald Islands' ),
                    (b'VA' , b'Vatican City State' ),
                    (b'HN' , b'Honduras' ),
                    (b'HK' , b'Hong Kong' ),
                    (b'HU' , b'Hungary' ),
                    (b'IS' , b'Iceland' ),
                    (b'IN' , b'India' ),
                    (b'ID' , b'Indonesia' ),
                    (b'IR' , b'Iran Islamic Republic of' ),
                    (b'IQ' , b'Iraq' ),
                    (b'IE' , b'Ireland' ),
                    (b'IM' , b'Isle of Man' ),
                    (b'IL' , b'Israel' ),
                    (b'IT' , b'Italy' ),
                    (b'JM' , b'Jamaica' ),
                    (b'JP' , b'Japan' ),
                    (b'JE' , b'Jersey' ),
                    (b'JO' , b'Jordan' ),
                    (b'KZ' , b'Kazakhstan' ),
                    (b'KE' , b'Kenya' ),
                    (b'KI' , b'Kiribati' ),
                    (b'KP' , b'Korea Democratic Peoples Republic of' ),
                    (b'KR' , b'Korea Republic of' ),
                    (b'KW' , b'Kuwait' ),
                    (b'KG' , b'Kyrgyzstan' ),
                    (b'LA' , b'Laos People Democratic Republic' ),
                    (b'LV' , b'Latvia' ),
                    (b'LB' , b'Lebanon' ),
                    (b'LS' , b'Lesotho' ),
                    (b'LR' , b'Liberia' ),
                    (b'LY' , b'Libyan Arab Jamahiriya' ),
                    (b'LI' , b'Liechtenstein' ),
                    (b'LT' , b'Lithuania' ),
                    (b'LU' , b'Luxembourg' ),
                    (b'MO' , b'Macao' ),
                    (b'MK' , b'Macedonia The Former Yugoslav Republic of' ),
                    (b'MG' , b'Madagascar' ),
                    (b'MW' , b'Malawi' ),
                    (b'MY' , b'Malaysia' ),
                    (b'MV' , b'Maldives' ),
                    (b'ML' , b'Mali' ),
                    (b'MT' , b'Malta' ),
                    (b'MH' , b'Marshall Islands' ),
                    (b'MQ' , b'Martinique' ),
                    (b'MR' , b'Mauritania' ),
                    (b'MU' , b'Mauritius' ),
                    (b'YT' , b'Mayotte' ),
                    (b'MX' , b'Mexico' ),
                    (b'FM' , b'Micronesia' ),
                    (b'MD' , b'Moldova' ),
                    (b'MC' , b'Monaco' ),
                    (b'MN' , b'Mongolia' ),
                    (b'ME' , b'Montenegro' ),
                    (b'MS' , b'Montserrat' ),
                    (b'MA' , b'Morocco' ),
                    (b'MZ' , b'Mozambique' ),
                    (b'MM' , b'Myanmar' ),
                    (b'NA' , b'Namibia' ),
                    (b'NR' , b'Nauru' ),
                    (b'NP' , b'Nepal' ),
                    (b'NL' , b'Netherlands' ),
                    (b'AN' , b'Netherlands Antilles' ),
                    (b'NC' , b'New Caledonia' ),
                    (b'NZ' , b'New Zealand' ),
                    (b'NI' , b'Nicaragua' ),
                    (b'NE' , b'Niger' ),
                    (b'NG' , b'Nigeria' ),
                    (b'NU' , b'Niue' ),
                    (b'NF' , b'Norfolk Island' ),
                    (b'MP' , b'Northern Mariana Islands' ),
                    (b'NO' , b'Norway' ),
                    (b'OM' , b'Oman' ),
                    (b'PK' , b'Pakistan' ),
                    (b'PW' , b'Palau' ),
                    (b'PS' , b'Palestinian Territory Occupied' ),
                    (b'PA' , b'Panama' ),
                    (b'PG' , b'Papua New Guinea' ),
                    (b'PY' , b'Paraguay' ),
                    (b'PE' , b'Peru' ),
                    (b'PH' , b'Philippines' ),
                    (b'PN' , b'Pitcairn' ),
                    (b'PL' , b'Poland' ),
                    (b'PT' , b'Portugal' ),
                    (b'PR' , b'Puerto Rico' ),
                    (b'QA' , b'Qatar' ),
                    (b'RE' , b'Reunion' ),
                    (b'RO' , b'Romania' ),
                    (b'RU' , b'Russian Federation' ),
                    (b'RW' , b'Rwanda' ),
                    (b'SH' , b'Saint Helena' ),
                    (b'KN' , b'Saint Kitts and Nevis' ),
                    (b'LC' , b'Saint Lucia' ),
                    (b'PM' , b'Saint Pierre and Miquelon' ),
                    (b'VC' , b'Saint Vincent and The Grenadines' ),
                    (b'WS' , b'Samoa' ),
                    (b'SM' , b'San Marino' ),
                    (b'ST' , b'Sao Tome and Principe' ),
                    (b'SA' , b'Saudi Arabia' ),
                    (b'SN' , b'Senegal' ),
                    (b'RS' , b'Serbia' ),
                    (b'SC' , b'Seychelles' ),
                    (b'SL' , b'Sierra Leone' ),
                    (b'SG' , b'Singapore' ),
                    (b'SK' , b'Slovakia' ),
                    (b'SI' , b'Slovenia' ),
                    (b'SB' , b'Solomon Islands' ),
                    (b'SO' , b'Somalia' ),
                    (b'ZA' , b'South Africa' ),
                    (b'GS' , b'South Georgia and The South Sandwich Islands' ),
                    (b'ES' , b'Spain' ),
                    (b'LK' , b'Sri Lanka' ),
                    (b'SD' , b'Sudan' ),
                    (b'SR' , b'Suriname' ),
                    (b'SJ' , b'Svalbard and Jan Mayen' ),
                    (b'SZ' , b'Swaziland' ),
                    (b'SE' , b'Sweden' ),
                    (b'CH' , b'Switzerland' ),
                    (b'SY' , b'Syrian Arab Republic' ),
                    (b'TW' , b'Taiwan Province of China' ),
                    (b'TJ' , b'Tajikistan' ),
                    (b'TZ' , b'Tanzania United Republic of' ),
                    (b'TH' , b'Thailand' ),
                    (b'TL' , b'Timor leste' ),
                    (b'TG' , b'Togo' ),
                    (b'TK' , b'Tokelau' ),
                    (b'TO' , b'Tonga' ),
                    (b'TT' , b'Trinidad and Tobago' ),
                    (b'TN' , b'Tunisia' ),
                    (b'TR' , b'Turkey' ),
                    (b'TM' , b'Turkmenistan' ),
                    (b'TC' , b'Turks and Caicos Islands' ),
                    (b'TV' , b'Tuvalu' ),
                    (b'UG' , b'Uganda' ),
                    (b'UA' , b'Ukraine' ),
                    (b'AE' , b'United Arab Emirates' ),
                    (b'GB' , b'United Kingdom' ),
                    (b'US' , b'United States' ),
                    (b'UM' , b'United States Minor Outlying Islands' ),
                    (b'UY' , b'Uruguay' ),
                    (b'UZ' , b'Uzbekistan' ),
                    (b'VU' , b'Vanuatu' ),
                    (b'VE' , b'Venezuela' ),
                    (b'VN' , b'Viet Nam' ),
                    (b'VG' , b'Virgin Islands British' ),
                    (b'VI' , b'Virgin Islands US' ),
                    (b'WF' , b'Wallis and Futuna' ),
                    (b'EH' , b'Western Sahara' ),
                    (b'YE' , b'Yemen' ),
                    (b'ZM' , b'Zambia' ),
                    (b'ZW' , b'Zimbabwe') ] )),
                ('country_codes', models.CharField(verbose_name="Country Code", max_length=100,
                 choices = [                
                    
                    (b'297', b'Aruba'),
                    (b'93', b'fghanistan'),
                    (b'244', b'Angola'),
                    (b'1264', b'Anguilla'),
                    (b'358', b'Aland Islands'),
                    (b'355', b'Albania'),
                    (b'376', b'Andorra'),
                    (b'971', b'United Arab Emirates'),
                    (b'54', b'Argentina'),
                    (b'374', b'Armenia'),
                    (b'1684', b'American Samoa'),
                    (b'1268', b'Antigua and Barbuda'),
                    (b'61', b'Australia'),
                    (b'43', b'Austria'),
                    (b'994', b'Azerbaijan'),
                    (b'257', b'Burundi'),
                    (b'32', b'Belgium'),
                    (b'229', b'Benin'),
                    (b'226', b'Burkina Faso'),
                    (b'880', b'Bangladesh'),
                    (b'359', b'Bulgaria'),
                    (b'973', b'Bahrain'),
                    (b'1242', b'Bahamas'),
                    (b'387', b'Bosnia and Herzegovina'),
                    (b'590', b'Saint Barthelemy'),
                    (b'375', b'Belarus'),
                    (b'501', b'Belize'),
                    (b'1441', b'Bermuda'),
                    (b'591', b'Bolivia'),
                    (b'55', b'Brazil'),
                    (b'1246', b'Barbados'),
                    (b'673', b'Brunei'),
                    (b'975', b'Bhutan'),
                    (b'267', b'Botswana'),
                    (b'236', b'Central African Republic'),
                    (b'1', b'Canada'),
                    (b'61', b'Cocos (Keeling) Islands'),
                    (b'41', b'Switzerland'),
                    (b'56', b'Chile'),
                    (b'86', b'China'),
                    (b'225', b'Ivory Coast'),
                    (b'237', b'Cameroon'),
                    (b'243', b'DR Congo'),
                    (b'242', b'Republic of the Congo'),
                    (b'682', b'Cook Islands'),
                    (b'57', b'Colombia'),
                    (b'269', b'Comoros'),
                    (b'238', b'ape Verde'),
                    (b'506', b'Costa Rica'),
                    (b'53', b'Cuba'),
                    (b'5999', b'Curacao'),
                    (b'61', b'Christmas Island'),
                    (b'1345', b'Cayman Islands'),
                    (b'357', b'Cyprus'),
                    (b'420', b'Czech Republic'),
                    (b'49', b'Germany'),
                    (b'253', b'Djibouti'),
                    (b'1767', b'Dominica'),
                    (b'45', b'Denmark'),
                    (b'1809', b'Dominican Republic'),
                    (b'1829', b'Dominican Republic'),
                    (b'1849', b'Dominican Republic'),
                    (b'213', b'Algeria'),
                    (b'593', b'Ecuador'),
                    (b'20', b'Egypt'),
                    (b'291', b'Eritrea'),
                    (b'212', b'Western Sahara'),
                    (b'34', b'Spain'),
                    (b'372', b'Estonia'),
                    (b'251', b'Ethiopia'),
                    (b'358', b'Finland'),
                    (b'679', b'Fiji'),
                    (b'500', b'Falkland Islands'),
                    (b'33', b'France'),
                    (b'298', b'Faroe Islands'),
                    (b'691', b'Micronesia'),
                    (b'241', b'Gabon'),
                    (b'44', b'United Kingdom'),
                    (b'995', b'Georgia'),
                    (b'44', b'Guernsey'),
                    (b'233', b'Ghana'),
                    (b'350', b'Gibraltar'),
                    (b'224', b'Guinea'),
                    (b'590', b'Guadeloupe'),
                    (b'220', b'Gambia'),
                    (b'245', b'Guinea-Bissau'),
                    (b'240', b'Equatorial Guinea'),
                    (b'30', b'Greece'),
                    (b'1473', b'Grenada'),
                    (b'299', b'Greenland'),
                    (b'502', b'Guatemala'),
                    (b'594', b'French Guiana'),
                    (b'1671', b'Guam'),
                    (b'592', b'Guyana'),
                    (b'852', b'Hong Kong'),
                    (b'504', b'Honduras'),
                    (b'385', b'Croatia'),
                    (b'509', b'Haiti'),
                    (b'36', b'Hungary'),
                    (b'62', b'Indonesia'),
                    (b'44', b'Isle of Man'),
                    (b'91', b'India'),
                    (b'246', b'British Indian Ocean Territory'),
                    (b'353', b'Ireland'),
                    (b'98', b'Iran'),
                    (b'964', b'Iraq'),
                    (b'354', b'Iceland'),
                    (b'972', b'Israel'),
                    (b'39', b'Italy'),
                    (b'1876', b'Jamaica'),
                    (b'44', b'Jersey'),
                    (b'962', b'Jordan'),
                    (b'81', b'Japan'),
                    (b'76', b'Kazakhstan'),
                    (b'77', b'Kazakhstan'),
                    (b'254', b'Kenya'),
                    (b'996', b'Kyrgyzstan'),
                    (b'855', b'Cambodia'),
                    (b'686', b'Kiribati'),
                    (b'1869', b'Saint Kitts and Nevis'),
                    (b'82', b'South Korea'),
                    (b'383', b'Kosovo'),
                    (b'965', b'Kuwait'),
                    (b'856', b'Laos'),
                    (b'961', b'Lebanon'),
                    (b'231', b'Liberia'),
                    (b'218', b'Libya'),
                    (b'1758', b'Saint Lucia'),
                    (b'423', b'Liechtenstein'),
                    (b'94', b'Sri Lanka'),
                    (b'266', b'Lesotho'),
                    (b'370', b'Lithuania'),
                    (b'352', b'Luxembourg'),
                    (b'371', b'Latvia'),
                    (b'853', b'Macau'),
                    (b'590', b'Saint Martin'),
                    (b'212', b'Morocco'),
                    (b'377', b'Monaco'),
                    (b'373', b'Moldova'),
                    (b'261', b'Madagascar'),
                    (b'960', b'Maldives'),
                    (b'52', b'Mexico'),
                    (b'692', b'Marshall Islands'),
                    (b'389', b'Macedonia'),
                    (b'223', b'Mali'),
                    (b'356', b'Malta'),
                    (b'95', b'Myanmar'),
                    (b'382', b'Montenegro'),
                    (b'976', b'Mongolia'),
                    (b'1670', b'Northern Mariana Islands'),
                    (b'258', b'Mozambique'),
                    (b'222', b'Mauritania'),
                    (b'1664', b'Montserrat'),
                    (b'596', b'Martinique'),
                    (b'230', b'Mauritius'),
                    (b'265', b'Malawi'),
                    (b'60', b'Malaysia'),
                    (b'262', b'Mayotte'),
                    (b'264', b'Namibia'),
                    (b'687', b'New Caledonia'),
                    (b'227', b'Niger'),
                    (b'672', b'Norfolk Island'),
                    (b'234', b'Nigeria'),
                    (b'505', b'Nicaragua'),
                    (b'683', b'Niue'),
                    (b'31', b'Netherlands'),
                    (b'47', b'Norway'),
                    (b'977', b'Nepal'),
                    (b'674', b'Nauru'),
                    (b'64', b'New Zealand'),
                    (b'968', b'Oman'),
                    (b'92', b'Pakistan'),
                    (b'507', b'Panama'),
                    (b'64', b'Pitcairn Islands'),
                    (b'51', b'Peru'),
                    (b'63', b'Philippines'),
                    (b'680', b'Palau'),
                    (b'675', b'Papua New Guinea'),
                    (b'48', b'Poland'),
                    (b'1787', b'Puerto Rico'),
                    (b'1939', b'Puerto Rico'),
                    (b'850', b'North Korea'),
                    (b'351', b'Portugal'),
                    (b'595', b'Paraguay'),
                    (b'970', b'Palestine'),
                    (b'689', b'French Polynesia'),
                    (b'974', b'Qatar'),
                    (b'262', b'Reunion'),
                    (b'40', b'Romania'),
                    (b'7', b'Russia'),
                    (b'250', b'Rwanda'),
                    (b'966', b'Saudi Arabia'),
                    (b'249', b'Sudan'),
                    (b'221', b'Senegal'),
                    (b'65', b'Singapore'),
                    (b'500', b'South Georgia'),
                    (b'4779', b'Svalbard and Jan Mayen'),
                    (b'677', b'Solomon Islands'),
                    (b'232', b'Sierra Leone'),
                    (b'503', b'El Salvador'),
                    (b'378', b'San Marino'),
                    (b'252', b'Somalia'),
                    (b'508', b'Saint Pierre and Miquelon'),
                    (b'381', b'Serbia'),
                    (b'211', b'South Sudan'),
                    (b'239', b'Sao Tome and Principe'),
                    (b'597', b'Suriname'),
                    (b'421', b'Slovakia'),
                    (b'386', b'Slovenia'),
                    (b'46', b'Sweden'),
                    (b'268', b'Swaziland'),
                    (b'1721', b'Sint Maarten'),
                    (b'248', b'Seychelles'),
                    (b'963', b'Syria'),
                    (b'1649', b'Turks and Caicos Islands'),
                    (b'235', b'Chad'),
                    (b'228', b'Togo'),
                    (b'66', b'Thailand'),
                    (b'992', b'Tajikistan'),
                    (b'690', b'Tokelau'),
                    (b'993', b'Turkmenistan'),
                    (b'670', b'TimorLeste'),
                    (b'676', b'Tonga'),
                    (b'1868', b'Trinidad and Tobago'),
                    (b'216', b'Tunisia'),
                    (b'90', b'Turkey'),
                    (b'688', b'Tuvalu'),
                    (b'886', b'Taiwan'),
                    (b'255', b'Tanzania'),
                    (b'256', b'Uganda'),
                    (b'380', b'Ukraine'),
                    (b'598', b'Uruguay'),
                    (b'1', b'United States'),
                    (b'998', b'Uzbekistan'),
                    (b'3906698', b'Vatican City'),
                    (b'379', b'Vatican City'),
                    (b'1784', b'Saint Vincent and the Grenadines'),
                    (b'58', b'Venezuela'),
                    (b'1284', b'British Virgin Islands'),
                    (b'1340', b'United States Virgin Islands'),
                    (b'84', b'Vietnam'),
                    (b'678', b'Vanuatu'),
                    (b'681', b'Wallis and Futuna'),
                    (b'685', b'Samoa'),
                    (b'967', b'Yemen'),
                    (b'27', b'South Africa'),
                    (b'260', b'Zambia'),
                    (b'263', b'Zimbabwe') ] )),
                ('phone_number', models.CharField(verbose_name="Phone Number", max_length=100)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
