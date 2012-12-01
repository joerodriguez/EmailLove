#EmailLove

Changing email providers or using multiple email providers typically is a pain in the ass since each provider has a different api and response. You end up writing new code for each provider which means that switching providers is thought of as a chore. EmailLove helps to fix this issue by providing a single api to access all popular email providers. Some of the features I hope to include are:

* Sending text add/or html emails
* Sending attachments
* Retrieving unsubscribe lists
* Retrieving bounce lists
* Retrieving spam report lists
* Pull open, click and other analytics

## Providers

This is the current list of providers. Feel free to add a provider, look at the other providers for examples.

* Mailgun (mailgun.net)
* SendGrid (sendgrid.net)
* MailJet (mailjet.net)
* Postmark (http://postmarkapp.com/)
* Amazon SES (http://aws.amazon.com/ses/)

## Install

* Fork or use this version
* pip install -e https://github.com/ryanrdetzel/EmailLove.git@master#egg=EmailLove  (the version on pypy is out of date)
* Setup enviroment variables if you want to run the tests
* See example below or look in the test directory


## Quick example

```python
lover = EmailLove()
sendgrid = SendGrid(username=os.environ.get('SENDGRID_USER'),¬           
                    password=os.environ.get('SENDGRID_PASS'))
mailgun = MailGun(api_key=os.environ.get('MAILGUN_APIKEY'),¬             
                  domain=os.environ.get('MAILGUN_DOMAIN'))
                
lover.providers.append(sendgrid)
lover.providers.append(mailgun)

lover.send({¬                                        
    'subject': "I love email.",¬                                            
    'from': "someone@somewhere.com", ¬                                           
    'to': [("ryan@magicmail.com,'Ryan Detzel')],¬                                         
    'text': 'EmailLove sendgrid text message',¬                          
    'html': '<b>EmailLove</b> sendgrid html <em>message</em>',¬          
})¬

lover.current_provider = mailgun

lover.send({¬                                        
    'subject': "I love email.",¬                                            
    'from': "someone@somewhere.com", ¬                                           
    'to': [("ryan@magicmail.com,'Ryan Detzel')],¬                                         
    'text': 'EmailLove mailgun text message',¬                          
    'html': '<b>EmailLove</b> mailgun html <em>message</em>',¬          
})¬
```

This example will send one email from sendgrid and then send another email from mailgun.

## Use cases

* Sending certain emails from certain accounts. Transactional vs marketing.
* Switching providers quickly
* Not hitting email limits on certain accounts(SES for example)
* Queue up the emails if they fail and try another provider
