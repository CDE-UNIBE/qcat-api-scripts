import pytest


@pytest.fixture()
def api_list_1():
    # results[0] corresponds to api_details_1
    return {
      "count": 1596,
      "next": "http://localhost:8000/en/api/v2/questionnaires/?format=json&page=2",
      "previous": "",
      "results": [
        {
          "name": "Contour Trench Bund",
          "updated": "2017-08-17T21:23:46.387708Z",
          "code": "technologies_1724",
          "url": "/en/wocat/technologies/view/technologies_1724/",
          "details": "/en/api/v2/questionnaires/technologies_1724/"
        },
        {
          "name": "Stone wall",
          "updated": "2017-07-04T10:45:20.110884Z",
          "code": "technologies_1723",
          "url": "/en/wocat/technologies/view/technologies_1723/",
          "details": "/en/api/v2/questionnaires/technologies_1723/"
        },
        {
          "name": "Cultivation of Hing (Ferula assa-foetida) in the watershed",
          "updated": "2017-01-04T15:43:43.545844Z",
          "code": "technologies_1306",
          "url": "/en/wocat/technologies/view/technologies_1306/",
          "details": "/en/api/v2/questionnaires/technologies_1306/"
        },
        {
          "name": "Community bakery",
          "updated": "2016-12-27T10:02:39.133822Z",
          "code": "technologies_1718",
          "url": "/en/wocat/technologies/view/technologies_1718/",
          "details": "/en/api/v2/questionnaires/technologies_1718/"
        },
        {
          "name": "Roof rain water harvesting",
          "updated": "2017-07-04T11:58:55.158672Z",
          "code": "technologies_1728",
          "url": "/en/wocat/technologies/view/technologies_1728/",
          "details": "/en/api/v2/questionnaires/technologies_1728/"
        },
        {
          "name": "Kanda",
          "updated": "2017-06-24T13:02:45.858958Z",
          "code": "technologies_1659",
          "url": "/en/wocat/technologies/view/technologies_1659/",
          "details": "/en/api/v2/questionnaires/technologies_1659/"
        },
        {
          "name": "Passive Solar House (PSH)",
          "updated": "2017-01-03T09:30:48.052382Z",
          "code": "technologies_1602",
          "url": "/en/wocat/technologies/view/technologies_1602/",
          "details": "/en/api/v2/questionnaires/technologies_1602/"
        },
        {
          "name": "Keyhole  Garden",
          "updated": "2017-07-04T10:10:11.930470Z",
          "code": "technologies_1722",
          "url": "/en/wocat/technologies/view/technologies_1722/",
          "details": "/en/api/v2/questionnaires/technologies_1722/"
        },
        {
          "name": "Irrigation of uplands through Hydraulic Flange Pump",
          "updated": "2017-07-04T13:19:02.519357Z",
          "code": "technologies_1731",
          "url": "/en/wocat/technologies/view/technologies_1731/",
          "details": "/en/api/v2/questionnaires/technologies_1731/"
        },
        {
          "name": "Terracing in Watershed",
          "updated": "2017-07-04T12:20:28.469450Z",
          "code": "technologies_1732",
          "url": "/en/wocat/technologies/view/technologies_1732/",
          "details": "/en/api/v2/questionnaires/technologies_1732/"
        },
        {
          "name": "Staggered Contour Trench",
          "updated": "2017-07-04T10:12:08.008568Z",
          "code": "technologies_1715",
          "url": "/en/wocat/technologies/view/technologies_1715/",
          "details": "/en/api/v2/questionnaires/technologies_1715/"
        },
        {
          "name": "Contour Tied Trench",
          "updated": "2017-06-24T13:29:32.806347Z",
          "code": "technologies_1661",
          "url": "/en/wocat/technologies/view/technologies_1661/",
          "details": "/en/api/v2/questionnaires/technologies_1661/"
        },
        {
          "name": "Terraces with improved seed and fertilizer application",
          "updated": "2017-06-22T09:22:18.923779Z",
          "code": "technologies_607",
          "url": "/en/wocat/technologies/view/technologies_607/",
          "details": "/en/api/v2/questionnaires/technologies_607/"
        },
        {
          "name": "Alfalfa intercropping in terraced fruit orchard",
          "updated": "2017-05-30T12:33:38.576564Z",
          "code": "technologies_1198",
          "url": "/en/wocat/technologies/view/technologies_1198/",
          "details": "/en/api/v2/questionnaires/technologies_1198/"
        },
        {
          "name": "Micro irrigation in poplar plantation",
          "updated": "2017-01-03T09:07:39.319114Z",
          "code": "technologies_1603",
          "url": "/en/wocat/technologies/view/technologies_1603/",
          "details": "/en/api/v2/questionnaires/technologies_1603/"
        },
        {
          "name": "Establishment of improved orchards and vineyards ",
          "updated": "2017-06-22T18:57:24.702707Z",
          "code": "technologies_669",
          "url": "/en/wocat/technologies/view/technologies_669/",
          "details": "/en/api/v2/questionnaires/technologies_669/"
        },
        {
          "name": "Rehabilitation  of degraded pastures with alfalfa",
          "updated": "2017-06-22T09:12:26.253675Z",
          "code": "technologies_672",
          "url": "/en/wocat/technologies/view/technologies_672/",
          "details": "/en/api/v2/questionnaires/technologies_672/"
        },
        {
          "name": "Riverbank stabilization",
          "updated": "2017-01-05T07:53:11.048457Z",
          "code": "technologies_1285",
          "url": "/en/wocat/technologies/view/technologies_1285/",
          "details": "/en/api/v2/questionnaires/technologies_1285/"
        },
        {
          "name": "Proclamation of the protected area in Albania_ Prespa National Park. Decision of the Council of Ministers No. 80, date 18.02.1999|",
          "updated": "2010-11-12T05:31:47Z",
          "code": "unccd_156",
          "url": "/en/unccd/view/unccd_156/",
          "details": "/en/api/v2/questionnaires/unccd_156/"
        },
        {
          "name": "EEG's Million Tree Campaign",
          "updated": "2010-10-11T05:30:50Z",
          "code": "unccd_260",
          "url": "/en/unccd/view/unccd_260/",
          "details": "/en/api/v2/questionnaires/unccd_260/"
        },
        {
          "name": "Ø¥Ø¹Ø¯Ø§Ø¯ Ù‚Ø§Ø¦Ù…Ø© Ø¨Ø§Ù„Ù†Ø¨Ø§ØªØ§Øª Ø§Ù„Ù…Ù‡Ø¯Ø¯Ø© Ø¨Ø§Ù„Ø§Ù†Ù‚Ø±Ø§Ø¶\nÙ…Ø³Ø­ Ø§Ù„ØºØ·Ø§Ø¡ Ø§Ù„Ù†Ø¨Ø§ØªÙŠ ÙÙŠ Ø¯ÙˆÙ„Ø© Ø§Ù„Ø§Ù…Ø§Ø±Ø§Øª Ø§Ù„Ø¹Ø±Ø¨ÙŠØ© Ø§Ù„Ù…ØªØ­Ø¯Ø©\nØªØ­Ø¯ÙŠØ« Ø§Ù„Ø§Ø³ØªØ±Ø§ØªÙŠØ¬ÙŠØ© Ø§Ù„ÙˆØ·Ù†ÙŠØ© Ù„Ù…ÙƒØ§ÙØ­Ø© Ø§Ù„ØªØµØ­Ø±",
          "updated": "2010-11-11T01:30:58Z",
          "code": "unccd_176",
          "url": "/en/unccd/view/unccd_176/",
          "details": "/en/api/v2/questionnaires/unccd_176/"
        },
        {
          "name": "Riego por curvas de nivel en mallines ",
          "updated": "2016-12-05T16:18:48.194153Z",
          "code": "unccd_214",
          "url": "/en/unccd/view/unccd_214/",
          "details": "/en/api/v2/questionnaires/unccd_214/"
        },
        {
          "name": "ImplantaciÃ³n de pasturas permanentes",
          "updated": "2016-12-05T16:15:56.704084Z",
          "code": "unccd_193",
          "url": "/en/unccd/view/unccd_193/",
          "details": "/en/api/v2/questionnaires/unccd_193/"
        },
        {
          "name": "Estufa a leÃ±a de alto rendimiento calÃ³rico",
          "updated": "2016-12-05T16:10:59.208648Z",
          "code": "unccd_205",
          "url": "/en/unccd/view/unccd_205/",
          "details": "/en/api/v2/questionnaires/unccd_205/"
        },
        {
          "name": "Uso de cobertizos para pariciones.",
          "updated": "2016-12-05T15:14:19.029240Z",
          "code": "unccd_430",
          "url": "/en/unccd/view/unccd_430/",
          "details": "/en/api/v2/questionnaires/unccd_430/"
        }
      ]
    }


@pytest.fixture()
def api_details_1():
    # corresponds to result[0] of api_list_1
    return {
      "section_general_information": {
        "label": "General Information",
        "children": {
          "tech__1": {
            "label": "General information",
            "children": {
              "tech__0__1": {
                "label": "Image",
                "children": {
                  "qg_image": {
                    "label": "",
                    "children": {
                      "image": {
                        "label": "Image",
                        "value": ""
                      },
                      "image_caption": {
                        "label": "Caption, explanation of photo",
                        "value": ""
                      },
                      "image_comments": {
                        "label": "Further comments",
                        "value": ""
                      },
                      "image_date": {
                        "label": "Date",
                        "value": ""
                      },
                      "image_location": {
                        "label": "Location",
                        "value": ""
                      },
                      "image_photographer": {
                        "label": "Name of photographer",
                        "value": ""
                      },
                      "image_target": {
                        "label": "Name of photographer",
                        "value": ""
                      }
                    }
                  }
                }
              },
              "tech__1__1": {
                "label": "Name of the SLM Technology (hereafter referred to as the Technology)",
                "children": {
                  "qg_name": {
                    "label": "",
                    "children": {
                      "name": {
                        "label": "Name",
                        "value": [
                          {
                            "in_list": True,
                            "is_name": True,
                            "additional_translations": {},
                            "key": "Name",
                            "value": "Contour Trench Bund",
                            "template": "raw"
                          }
                        ]
                      },
                      "name_local": {
                        "label": "Locally used name",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Locally used name",
                            "value": "Chuquorak Band Khaki (Dari)",
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  },
                  "qg_location": {
                    "label": "",
                    "children": {
                      "country": {
                        "label": "Country",
                        "value": [
                          {
                            "in_list": True,
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Country",
                            "value": "Afghanistan"
                          }
                        ]
                      },
                      "state_province": {
                        "label": "Region/ State/ Province",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Region/ State/ Province",
                            "value": "Sar_e_Ahangaran, Bamyan center",
                            "template": "raw"
                          }
                        ]
                      },
                      "further_location": {
                        "label": "Further specification of location (e.g. municipality, town, etc.), if relevant",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Further specification of location",
                            "value": None,
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  },
                  "qg_import": {
                    "label": "",
                    "children": {
                      "import_old_code": {
                        "label": "None",
                        "value": ""
                      }
                    }
                  }
                }
              },
              "tech__1__2": {
                "label": "Contact details of resource persons and institutions involved in the assessment and documentation of the Technology",
                "children": {
                  "tech_qg_184": {
                    "label": "Key resource person(s)",
                    "children": {
                      "user_resourceperson_type": {
                        "label": "Specify the key resource person",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Specify the key resource person",
                            "values": [
                              "SLM specialist"
                            ]
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Specify the key resource person",
                            "values": [
                              "SLM specialist"
                            ]
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Specify the key resource person",
                            "values": [
                              "SLM specialist"
                            ]
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Specify the key resource person",
                            "values": [
                              "SLM specialist"
                            ]
                          }
                        ]
                      },
                      "user_resourceperson_other": {
                        "label": "Other (specify)",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Other (specify)",
                            "value": None
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Other (specify)",
                            "value": None
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Other (specify)",
                            "value": None
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Other (specify)",
                            "value": None
                          }
                        ]
                      },
                      "user_id": {
                        "label": "User ID",
                        "value": [
                          {
                            "additional_translations": {},
                            "value": "Aqila Haidery",
                            "user_id": "3006",
                            "unknown_user": False,
                            "template": "raw"
                          },
                          {
                            "additional_translations": {},
                            "value": "Sanjeev Bhuchar",
                            "user_id": "1572",
                            "unknown_user": False,
                            "template": "raw"
                          },
                          {
                            "additional_translations": {},
                            "value": "Madhav Dhakal",
                            "user_id": "512",
                            "unknown_user": False,
                            "template": "raw"
                          },
                          "\n"
                        ]
                      },
                      "person_lastname": {
                        "label": "Lastname / surname",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Lastname / surname",
                            "value": None
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Lastname / surname",
                            "value": None
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Lastname / surname",
                            "value": None
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Lastname / surname",
                            "value": "Ershad"
                          }
                        ]
                      },
                      "person_firstname": {
                        "label": "First name(s)",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "First name(s)",
                            "value": None
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "First name(s)",
                            "value": None
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "First name(s)",
                            "value": None
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "First name(s)",
                            "value": "Mustafa "
                          }
                        ]
                      },
                      "person_gender": {
                        "label": "Gender",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Gender",
                            "values": []
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Gender",
                            "values": []
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Gender",
                            "values": []
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Gender",
                            "values": [
                              "male"
                            ]
                          }
                        ]
                      },
                      "person_institution_name": {
                        "label": "Name of institution",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Name of institution",
                            "value": None
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Name of institution",
                            "value": None
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Name of institution",
                            "value": None
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Name of institution",
                            "value": "Catholic Relief Services"
                          }
                        ]
                      },
                      "person_address": {
                        "label": "Address",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Address",
                            "value": None
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Address",
                            "value": None
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Address",
                            "value": None
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Address",
                            "value": None
                          }
                        ]
                      },
                      "country": {
                        "label": "Country",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Country",
                            "value": ""
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Country",
                            "value": ""
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Country",
                            "value": ""
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Country",
                            "value": ""
                          }
                        ]
                      },
                      "person_phone_1": {
                        "label": "Phone no. 1",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Phone no. 1",
                            "value": None
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Phone no. 1",
                            "value": None
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Phone no. 1",
                            "value": None
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Phone no. 1",
                            "value": None
                          }
                        ]
                      },
                      "person_phone_2": {
                        "label": "Phone no. 2 (mobile)",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Phone no. 2 (mobile)",
                            "value": None
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Phone no. 2 (mobile)",
                            "value": None
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Phone no. 2 (mobile)",
                            "value": None
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Phone no. 2 (mobile)",
                            "value": None
                          }
                        ]
                      },
                      "person_email_1": {
                        "label": "E-mail 1",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "E-mail 1",
                            "value": None
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "E-mail 1",
                            "value": None
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "E-mail 1",
                            "value": None
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "E-mail 1",
                            "value": "mustafa.ershad@crs.org "
                          }
                        ]
                      },
                      "person_email_2": {
                        "label": "E-mail 2",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "E-mail 2",
                            "value": None
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "E-mail 2",
                            "value": None
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "E-mail 2",
                            "value": None
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "E-mail 2",
                            "value": None
                          }
                        ]
                      }
                    }
                  },
                  "qg_funding_project": {
                    "label": "",
                    "children": {
                      "funding_project": {
                        "label": "Name of project which facilitated the documentation/ evaluation of the Technology (if relevant)",
                        "value": ""
                      },
                      "funding_project_display": {
                        "label": "Name of project which facilitated the documentation/ evaluation of the Technology (if relevant)",
                        "value": ""
                      }
                    }
                  },
                  "qg_funding_institution": {
                    "label": "",
                    "children": {
                      "funding_institution": {
                        "label": "Name of the institution(s) which facilitated the documentation/ evaluation of the Technology (if relevant)",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Name of the institution(s) which facilitated the documentation/ evaluation of the Technology (if relevant)",
                            "value": 682,
                            "template": "raw"
                          },
                          {
                            "additional_translations": {},
                            "key": "Name of the institution(s) which facilitated the documentation/ evaluation of the Technology (if relevant)",
                            "value": 377,
                            "template": "raw"
                          }
                        ]
                      },
                      "funding_institution_display": {
                        "label": "Name of the institution(s) which facilitated the documentation/ evaluation of the Technology (if relevant)",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Name of the institution(s) which facilitated the documentation/ evaluation of the Technology (if relevant)",
                            "value": "Helvetas Swiss Intercooperation - Switzerland",
                            "template": "raw"
                          },
                          {
                            "additional_translations": {},
                            "key": "Name of the institution(s) which facilitated the documentation/ evaluation of the Technology (if relevant)",
                            "value": "Catholic Relief Services (CRS) - United States",
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  }
                }
              },
              "tech__1__3": {
                "label": "Conditions regarding the use of data documented through WOCAT",
                "children": {
                  "qg_accept_conditions": {
                    "label": "None",
                    "children": {
                      "date_documentation": {
                        "label": "When were the data compiled (in the field)?",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "When were the data compiled (in the field)?",
                            "value": "04/07/2011",
                            "template": "raw"
                          }
                        ]
                      },
                      "accept_conditions": {
                        "label": "The compiler and key resource person(s) accept the conditions regarding the use of data documented through WOCAT",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "The compiler and key resource person(s) accept the conditions regarding the use of data documented through WOCAT",
                            "value": "Yes",
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  }
                }
              },
              "tech__1__4": {
                "label": "Declaration on sustainability of the described Technology",
                "children": {
                  "tech_qg_156": {
                    "label": "",
                    "children": {
                      "tech_sustainability": {
                        "label": "Is the Technology described here problematic with regard to land degradation, so that it cannot be declared a sustainable land management technology?",
                        "value": ""
                      },
                      "tech_sustainability_indicate": {
                        "label": "Comments",
                        "value": ""
                      }
                    }
                  }
                }
              },
              "tech__1__5": {
                "label": "Reference to Questionnaire(s) on SLM Approaches",
                "children": {
                  "tech_qg__approaches": {
                    "label": "",
                    "children": {
                      "link_id": {
                        "label": "None",
                        "value": ""
                      }
                    }
                  }
                }
              },
              "tech__1__6": {
                "label": "Reference to/ comparison with other Technologies",
                "children": {}
              }
            }
          }
        }
      },
      "section_specifications": {
        "label": "Specifications",
        "children": {
          "tech__2": {
            "label": "Description of the SLM Technology",
            "children": {
              "tech__2__1": {
                "label": "Short description of the Technology",
                "children": {
                  "tech_qg_1": {
                    "label": "",
                    "children": {
                      "tech_definition": {
                        "label": "Definition of the Technology",
                        "value": [
                          {
                            "in_list": True,
                            "additional_translations": {},
                            "key": "Definition of the Technology",
                            "value": "Contour trench bund applied on contour lines of moderate slope to trap run-off to improve infiltration and reduce flash floods.",
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  }
                }
              },
              "tech__2__2": {
                "label": "Detailed description of the Technology",
                "children": {
                  "tech_qg_2": {
                    "label": "",
                    "children": {
                      "tech_description": {
                        "label": "Description",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Description",
                            "value": "The Contour Trench Bund technology is documented by Sustainable Land Management\r\nProject/HELVETAS Swiss Intercooperation with financial support of Swiss Agency for\r\nDevelopment and Cooperation(SDC) and close support and cooperation of the Catholic\r\nRelief Service (CRS). The technology was applied in Sar-e Ahengaran watershed of Bamyan centre, an area of 0.08 km2 as part of a watershed project by the Catholic Relief Services (CRS). The total watershed area is 67 ha. The project started in October 2009 involving the community with funding support from USAID and CRS. The project came to an end in March 2013.\r\n\r\nPurpose of the Technology: The main purpose of the contour trench bund technology is to reduce excessive surface runoff and improve infiltration. It also contributes to increased vegetation cover.\r\n\r\nEstablishment / maintenance activities and inputs: The main activities for this SLM technology include: site selection and technical planning in October 2009; demarcation of contour lines using A-frame and lime; and digging trenches and construction of soil bunds. The technology was established over 10 months. The project used a â€œCash for Workâ€ approach; local people were employed for construction works. Cost-wise, approximately 7,536 USD were spent on this technology (approximately 942 USD/ha) with 90% contribution from the project and 10% from the participating community. There have been no maintenance costs so far for this technology.\r\n\r\nDimensions of a trenches are: 0.7 m in depth, 1.2 m width, 3 m length and of the bunds: 0.45 m in height, 1.2 m in width, 100 m in length with 12 m spacing and 1.5 m vertical interval between two contour lines. Contour trenches were applied on hilly (16-30%) slopes at an altitude of 2500-3000 m. The technology is tolerant to temperature, seasonal rainfall, storms and droughts and sensitive to heavy rainfall events and floods. The soil in the watershed is sandy to loamy type, and infertile with a depth of 20-50 cm. The infiltration is medium.\r\n\r\nThe technology is part of the watershed management system. Other measures implemented included stone walls, cultivation of fodder grasses and ban on grazing and shrub cutting at the site. The land ownership (in the watershed) is communal with open access water rights. Medium scale land users, mainly men, applied the technology. Women and school children participated in meetings concerning awareness raising. There is also a watershed and pasture management committee for site management.\r\n\r\nNatural / human environment: The annual rainfall in the area is 250-500 mm. The agro-climate is semi-arid and temperate type with the longest growing period of 180 days from April to October. The people in this area are mainly poor. 10-50 % of all income comes from off-farm activities. Access to health, market and financial services is low and education, roads, transport, drinking water and sanitation facilities are moderate. Agriculture is of mixed type, subsistence and commercial based.",
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  }
                }
              },
              "tech__2__3": {
                "label": "Photos of the Technology",
                "children": {
                  "qg_photos": {
                    "label": "",
                    "children": {
                      "image": {
                        "label": "Image",
                        "value": [
                          {
                            "in_list": True,
                            "additional_translations": {},
                            "content_type": "image/jpeg",
                            "preview_image": "/upload/90/c/90c12693-efbd-4c41-acd6-bce6b63ece58.jpg",
                            "key": "Image",
                            "value": "/upload/16/b/16bd597b-ec1c-4ee2-bc49-f05cdb337e91.jpg",
                            "template": "raw"
                          },
                          {
                            "in_list": True,
                            "additional_translations": {},
                            "content_type": "image/jpeg",
                            "preview_image": "/upload/19/5/195e4989-3df5-4b36-b6b6-9754e5893f8f.jpg",
                            "key": "Image",
                            "value": "/upload/21/e/21ef5942-ae4b-469b-8834-907099cfccff.jpg",
                            "template": "raw"
                          }
                        ]
                      },
                      "image_caption": {
                        "label": "Caption, explanation of photo",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Caption, explanation of photo",
                            "value": "An overview of contour trench bund applied along the lines across the slope in Sar e Ahengaran of Bamyan centre through a watershed project by CRS (Catholic Relief Services)",
                            "template": "raw"
                          },
                          {
                            "additional_translations": {},
                            "key": "Caption, explanation of photo",
                            "value": "The photo shows trenches excavated across the slope and the dug soil used to make a bund on the lower part of the trenches",
                            "template": "raw"
                          }
                        ]
                      },
                      "image_comments": {
                        "label": "Further comments",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Further comments",
                            "value": None,
                            "template": "raw"
                          },
                          {
                            "additional_translations": {},
                            "key": "Further comments",
                            "value": None,
                            "template": "raw"
                          }
                        ]
                      },
                      "image_date": {
                        "label": "Date",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Date",
                            "value": "07/06/2011",
                            "template": "raw"
                          },
                          {
                            "additional_translations": {},
                            "key": "Date",
                            "value": "07/06/2011",
                            "template": "raw"
                          }
                        ]
                      },
                      "image_location": {
                        "label": "Location",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Location",
                            "value": "Sar-e-Ahangaran, Bamyan center",
                            "template": "raw"
                          },
                          {
                            "additional_translations": {},
                            "key": "Location",
                            "value": "Sar_e_Ahanaran, Bamyan center",
                            "template": "raw"
                          }
                        ]
                      },
                      "image_photographer": {
                        "label": "Name of photographer",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Name of photographer",
                            "value": None,
                            "template": "raw"
                          },
                          {
                            "additional_translations": {},
                            "key": "Name of photographer",
                            "value": None,
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  },
                  "qg_image_remarks": {
                    "label": "",
                    "children": {
                      "image_remarks": {
                        "label": "General remarks regarding photos",
                        "value": ""
                      }
                    }
                  }
                }
              },
              "tech__2__4": {
                "label": "Videos of the Technology",
                "children": {
                  "qg_videos": {
                    "label": "",
                    "children": {
                      "video_vimeo_id": {
                        "label": "Vimeo ID",
                        "value": ""
                      },
                      "video_description": {
                        "label": "Comments, short description",
                        "value": ""
                      },
                      "video_date": {
                        "label": "Date",
                        "value": ""
                      },
                      "video_location": {
                        "label": "Location",
                        "value": ""
                      },
                      "video_videographer": {
                        "label": "Name of videographer",
                        "value": ""
                      }
                    }
                  }
                }
              },
              "tech__2__5": {
                "label": "Country/ region/ locations where the Technology has been applied and which are covered by this assessment",
                "children": {
                  "qg_location": {
                    "label": "",
                    "children": {
                      "country": {
                        "label": "Country",
                        "value": [
                          {
                            "in_list": True,
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Country",
                            "value": "Afghanistan"
                          }
                        ]
                      },
                      "state_province": {
                        "label": "Region/ State/ Province",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Region/ State/ Province",
                            "value": "Sar_e_Ahangaran, Bamyan center"
                          }
                        ]
                      },
                      "further_location": {
                        "label": "Further specification of location (e.g. municipality, town, etc.), if relevant",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Further specification of location",
                            "value": None
                          }
                        ]
                      }
                    }
                  },
                  "tech_qg_3": {
                    "label": "",
                    "children": {
                      "tech_sites_considered": {
                        "label": "Number of sites considered/analysed in the documentation of this technology",
                        "value": ""
                      }
                    }
                  },
                  "qg_location_map": {
                    "label": "Add geo-referenced information on the map below",
                    "children": {
                      "location_map": {
                        "label": "Map",
                        "value": [
                          {
                            "is_geometry": True,
                            "configuration": "technologies",
                            "additional_translations": {},
                            "key": "Map",
                            "value": "{\"type\":\"FeatureCollection\",\"features\":[{\"type\":\"Feature\",\"id\":1499165591161,\"geometry\":{\"type\":\"Point\",\"coordinates\":[67.54596,34.444290000000024]},\"properties\":null}]}",
                            "map_url": "/en/wocat/technologies/view/technologies_1724/map/",
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  },
                  "tech_qg_225": {
                    "label": "",
                    "children": {
                      "location_comments": {
                        "label": "Comments",
                        "value": ""
                      }
                    }
                  }
                }
              },
              "tech__2__6": {
                "label": "Date of implementation",
                "children": {
                  "tech_qg_160": {
                    "label": "",
                    "children": {
                      "tech_implementation_year": {
                        "label": "Indicate year of implementation",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Indicate year of implementation",
                            "value": None,
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_implementation_decades": {
                        "label": "If precise year is not known, indicate approximate date",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "If precise year is not known, indicate approximate date",
                            "values": [
                              "less than 10 years ago (recently)"
                            ],
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  }
                }
              },
              "tech__2__7": {
                "label": "Introduction of the Technology",
                "children": {
                  "tech_qg_5": {
                    "label": "",
                    "children": {
                      "tech_who_implemented": {
                        "label": "Specify how the Technology was introduced",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Specify how the Technology was introduced",
                            "values": [
                              "through projects/ external interventions"
                            ],
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_who_implemented_other": {
                        "label": "other (specify)",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "other (specify)",
                            "value": None
                          }
                        ]
                      },
                      "tech_who_implemented_comments": {
                        "label": "Comments (type of project, etc.)",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Comments (type of project, etc.)",
                            "value": None,
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  }
                }
              }
            }
          },
          "tech__3": {
            "label": "Classification of the SLM Technology",
            "children": {
              "tech__3__1": {
                "label": "Main purpose(s) of the Technology",
                "children": {
                  "tech_qg_6": {
                    "label": "",
                    "children": {
                      "tech_main_purpose": {
                        "label": "Main purpose(s) of the Technology (land userâ€™s perspective)",
                        "value": [
                          {
                            "label_position": "none",
                            "additional_translations": {},
                            "key": "Main purpose(s) of the Technology (land userâ€™s perspective)",
                            "values": [
                              "protect a watershed/ downstream areas â€“ in combination with other Technologies",
                              "reduce risk of disasters"
                            ],
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_main_purpose_other": {
                        "label": "other (specify)",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "other (specify)",
                            "value": None
                          }
                        ]
                      }
                    }
                  }
                }
              },
              "tech__3__2": {
                "label": "Current land use type(s) where the Technology is applied",
                "children": {
                  "tech_qg_9": {
                    "label": "",
                    "children": {
                      "tech_landuse": {
                        "label": "Select land use type",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Land use type",
                            "values": [
                              [
                                "Grazing land",
                                "assets/img/pictos/land_5.png",
                                None,
                                "tech_lu_grazingland"
                              ]
                            ]
                          }
                        ]
                      }
                    }
                  },
                  "tech_qg_10": {
                    "label": "",
                    "children": {
                      "tech_lu_cropland_sub": {
                        "label": "Select category(ies) / code(s)",
                        "value": ""
                      },
                      "tech_lu_sub_other": {
                        "label": "other (specify)",
                        "value": ""
                      },
                      "tech_lu_cropland_specify": {
                        "label": "Main crops (cash and food crops)",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_11": {
                    "label": "",
                    "children": {
                      "tech_lu_grazingland_extensive": {
                        "label": "Extensive grazing land",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Extensive grazing land",
                            "values": [
                              "Semi-nomadism/ pastoralism"
                            ],
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_lu_grazingland_intensive": {
                        "label": "Intensive grazing/ fodder production",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Intensive grazing/ fodder production",
                            "values": [],
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_lu_sub_other": {
                        "label": "other (specify)",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "other (specify)",
                            "value": None
                          }
                        ]
                      },
                      "tech_lu_grazingland_specify": {
                        "label": "Main animal species and products",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Main animal species and products",
                            "value": " Sheeps, goats and cattle ",
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  },
                  "tech_qg_12": {
                    "label": "",
                    "children": {
                      "tech_lu_forest_natural": {
                        "label": "(Semi-)natural forests/ woodlands",
                        "value": ""
                      },
                      "tech_lu_forest_plantation": {
                        "label": "Tree plantation, afforestation",
                        "value": ""
                      },
                      "tech_lu_sub_other": {
                        "label": "other (specify)",
                        "value": ""
                      },
                      "tech_lu_forest_products": {
                        "label": "Products and services",
                        "value": ""
                      },
                      "tech_lu_forest_other": {
                        "label": "other (specify)",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_13": {
                    "label": "",
                    "children": {
                      "tech_lu_mixed_sub": {
                        "label": "Select category(ies) / code(s)",
                        "value": ""
                      },
                      "tech_lu_sub_other": {
                        "label": "other (specify)",
                        "value": ""
                      },
                      "tech_lu_mixed_specify": {
                        "label": "Main products/ services",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_14": {
                    "label": "",
                    "children": {
                      "tech_lu_settlements_sub": {
                        "label": "Select category(ies) / code(s)",
                        "value": ""
                      },
                      "tech_lu_sub_other": {
                        "label": "other (specify)",
                        "value": ""
                      },
                      "tech_lu_settlements_specify": {
                        "label": "Remarks",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_15": {
                    "label": "",
                    "children": {
                      "tech_lu_waterways_sub": {
                        "label": "Select category(ies) / code(s)",
                        "value": ""
                      },
                      "tech_lu_sub_other": {
                        "label": "other (specify)",
                        "value": ""
                      },
                      "tech_lu_waterways_specify": {
                        "label": "Main products/ services",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_16": {
                    "label": "",
                    "children": {
                      "tech_lu_specify": {
                        "label": "Specify",
                        "value": ""
                      },
                      "tech_lu_mines_specify": {
                        "label": "Main products",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_17": {
                    "label": "",
                    "children": {
                      "tech_lu_specify": {
                        "label": "Specify",
                        "value": ""
                      },
                      "tech_lu_unproductive_specify": {
                        "label": "Remarks",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_18": {
                    "label": "",
                    "children": {
                      "tech_lu_specify": {
                        "label": "Specify",
                        "value": ""
                      },
                      "tech_lu_other_specify": {
                        "label": "Remarks",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_7": {
                    "label": "",
                    "children": {
                      "tech_lu_comments": {
                        "label": "Comments",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Comments",
                            "value": "Major land use problems (compilerâ€™s opinion): Reduction of the vegetation cover causes flash floods and accelerated erosion. The water level goes down and there is no moisture in the soil.\r\n\r\nMajor land use problems (land usersâ€™ perception): Downstream flash flood and shortage of spring water due to overgrazing of the range-land.\r\n\r\nFuture (final) land use (after implementation of SLM Technology): Grazing land: Gi: Intensive grazing/ fodder production",
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_lu_change": {
                        "label": "If land use has changed due to the implementation of the Technology, indicate land use before implementation of the Technology",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "If land use has changed due to the implementation of the Technology, indicate land use before implementation of the Technology",
                            "value": "Grazing land: Ge: Extensive grazing land",
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  }
                }
              },
              "tech__3__3": {
                "label": "Further information about land use",
                "children": {
                  "tech_qg_19": {
                    "label": "",
                    "children": {
                      "tech_watersupply": {
                        "label": "Water supply for the land on which the Technology is applied",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Water supply for the land on which the Technology is applied",
                            "values": [
                              "mixed rainfed-irrigated"
                            ],
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_watersupply_other": {
                        "label": "other (e.g. post-flooding)",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "other (e.g. post-flooding)",
                            "value": None
                          }
                        ]
                      },
                      "tech_watersupply_comments": {
                        "label": "Comments",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Comments",
                            "value": None,
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_growing_seasons": {
                        "label": "Number of growing seasons per year",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Number of growing seasons per year",
                            "values": [
                              "1"
                            ],
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_growing_seasons_specify": {
                        "label": "Specify",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Specify",
                            "value": "Longest growing period in days: 180; Longest growing period from month to month: April to October",
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_livestock_density": {
                        "label": "Livestock density (if relevant)",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Livestock density (if relevant)",
                            "value": "10-25 LU /km2",
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  }
                }
              },
              "tech__3__4": {
                "label": "SLM group to which the Technology belongs",
                "children": {
                  "tech_qg_20": {
                    "label": "",
                    "children": {
                      "tech_slm_group": {
                        "label": "SLM group to which the Technology belongs",
                        "value": [
                          {
                            "label_position": "none",
                            "additional_translations": {},
                            "key": "SLM group",
                            "values": [
                              "improved ground/ vegetation cover",
                              "cross-slope measure"
                            ],
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_slm_group_other": {
                        "label": "other (specify)",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "other (specify)",
                            "value": None
                          }
                        ]
                      }
                    }
                  }
                }
              },
              "tech__3__5": {
                "label": "Spread of the Technology",
                "children": {
                  "tech_qg_4": {
                    "label": "",
                    "children": {
                      "tech_spread_tech": {
                        "label": "Specify the spread of the Technology",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Specify the spread of the Technology",
                            "values": [],
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_spread_area": {
                        "label": "If the Technology is evenly spread over an area, indicate approximate area covered",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "If the Technology is evenly spread over an area, indicate approximate area covered",
                            "values": [],
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_spread_tech_comments": {
                        "label": "Comments",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Comments",
                            "value": "Total area covered by the SLM Technology is 0.08 km2.",
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  }
                }
              },
              "tech__3__6": {
                "label": "SLM measures comprising the Technology",
                "children": {
                  "tech_qg_8": {
                    "label": "",
                    "children": {
                      "tech_measures": {
                        "label": "SLM measures comprising the Technology",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "SLM measures",
                            "values": [
                              [
                                "structural measures",
                                "assets/img/pictos/swc_1_struc.png",
                                None,
                                "tech_measures_structural"
                              ]
                            ]
                          }
                        ]
                      }
                    }
                  },
                  "tech_qg_21": {
                    "label": "",
                    "children": {
                      "tech_measures_agronomic_sub": {
                        "label": "Select category(ies) / code(s)",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_22": {
                    "label": "",
                    "children": {
                      "tech_measures_vegetative_sub": {
                        "label": "Select category(ies) / code(s)",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_23": {
                    "label": "",
                    "children": {
                      "tech_measures_structural_sub": {
                        "label": "Select category(ies) / code(s)",
                        "value": [
                          {
                            "label_position": "none",
                            "additional_translations": {},
                            "key": "SLM measures",
                            "values": [
                              "S2: Bunds, banks",
                              "S4: Level ditches, pits"
                            ],
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  },
                  "tech_qg_24": {
                    "label": "",
                    "children": {
                      "tech_measures_management_sub": {
                        "label": "Select category(ies) / code(s)",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_25": {
                    "label": "",
                    "children": {
                      "tech_stub": {
                        "label": "None",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_26": {
                    "label": "",
                    "children": {
                      "tech_measures_comments": {
                        "label": "Comments",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Comments",
                            "value": "Main measures: structural measures",
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  }
                }
              },
              "tech__3__7": {
                "label": "Main types of land degradation addressed by the Technology",
                "children": {
                  "tech_qg_27": {
                    "label": "",
                    "children": {
                      "tech_degradation": {
                        "label": "Select degradation type",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Degradation type",
                            "values": [
                              [
                                "soil erosion by water",
                                "assets/img/pictos/degra_watererosion.png",
                                None,
                                "degradation_erosion_water"
                              ]
                            ]
                          }
                        ]
                      }
                    }
                  },
                  "tech_qg_28": {
                    "label": "",
                    "children": {
                      "degradation_erosion_water_sub": {
                        "label": "Select category(ies) / code(s)",
                        "value": [
                          {
                            "label_position": "none",
                            "additional_translations": {},
                            "key": "Degradation type",
                            "values": [
                              "Wt: loss of topsoil/ surface erosion"
                            ],
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  },
                  "tech_qg_29": {
                    "label": "",
                    "children": {
                      "degradation_erosion_wind_sub": {
                        "label": "Select category(ies) / code(s)",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_30": {
                    "label": "",
                    "children": {
                      "degradation_chemical_sub": {
                        "label": "Select category(ies) / code(s)",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_31": {
                    "label": "",
                    "children": {
                      "degradation_physical_sub": {
                        "label": "Select category(ies) / code(s)",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_32": {
                    "label": "",
                    "children": {
                      "degradation_biological_sub": {
                        "label": "Select category(ies) / code(s)",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_33": {
                    "label": "",
                    "children": {
                      "degradation_water_sub": {
                        "label": "Select category(ies) / code(s)",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_231": {
                    "label": "",
                    "children": {
                      "tech_stub": {
                        "label": "None",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_34": {
                    "label": "",
                    "children": {
                      "degradation_comments": {
                        "label": "Comments",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Comments",
                            "value": "Main causes of degradation: over-exploitation of vegetation for domestic use, overgrazing",
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  }
                }
              },
              "tech__3__8": {
                "label": "Prevention, reduction, or restoration of land degradation",
                "children": {
                  "tech_qg_35": {
                    "label": "",
                    "children": {
                      "tech_prevention": {
                        "label": "Specify the goal of the Technology with regard to land degradation",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Specify the goal of the Technology with regard to land degradation",
                            "values": [
                              "reduce land degradation"
                            ],
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_prevention_comments": {
                        "label": "Comments",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Comments",
                            "value": None,
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  }
                }
              }
            }
          },
          "tech__4": {
            "label": "Technical specifications, implementation activities, inputs, and costs",
            "children": {
              "tech__4__1": {
                "label": "Technical drawing of the Technology",
                "children": {
                  "tech_qg_185": {
                    "label": "",
                    "children": {
                      "tech_drawing": {
                        "label": "Technical drawing",
                        "value": [
                          {
                            "additional_translations": {},
                            "content_type": "image/jpeg",
                            "preview_image": "/upload/f2/b/f2bad096-a06e-4fe6-b9c0-79a04ee27c3d.jpg",
                            "key": "Technical drawing",
                            "value": "/upload/1f/3/1f3fc447-5d17-4338-848b-d1ba6bba97e2.jpg",
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_drawing_author": {
                        "label": "Author",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Author",
                            "value": "Mustafa Ershad",
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_drawing_date": {
                        "label": "Date",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Date",
                            "value": None,
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  }
                }
              },
              "tech__4__2": {
                "label": "Technical specifications/ explanations of technical drawing",
                "children": {
                  "tech_qg_161": {
                    "label": "",
                    "children": {
                      "tech_specifications": {
                        "label": "Technical specifications (related to technical drawing)",
                        "value": [
                          {
                            "label_position": "none",
                            "additional_translations": {},
                            "key": "Technical specifications (related to technical drawing)",
                            "value": "The technical drawing of the Contour trench bund showing the layout and dimensions/spacing of the structures.\r\nDimensions of the trench and bund are as following:\r\nTrench specifications: \r\nDepth: 0.7 m, \r\nWidth: 1.2 m, Length: 3 m \r\nSoil bund specifications: \r\nHeight: 0.45 m \r\nWidth: 1.2 m\r\nLength: 100 m\r\nSpacing between contour lines: \r\nAbout 8 -12 m (depend on slop)\r\nVertical interval: \r\n1.5 m\r\n\r\nTechnical knowledge required for field staff / advisors: moderate\r\n\r\nTechnical knowledge required for land users: moderate\r\n\r\nMain technical functions: control of raindrop splash, control of dispersed runoff: retain / trap, increase of infiltration\r\n\r\nSecondary technical functions: reduction of slope length, increase of groundwater level / recharge of groundwater, sediment retention / trapping, sediment harvesting",
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  }
                }
              },
              "tech__4__3": {
                "label": "General information regarding the calculation of inputs and costs",
                "children": {
                  "tech_qg_217": {
                    "label": "",
                    "children": {
                      "tech_cost_calculation_base": {
                        "label": "Specify how costs and inputs were calculated",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_163": {
                    "label": "",
                    "children": {
                      "tech_perarea_size": {
                        "label": "Indicate size and area unit",
                        "value": ""
                      },
                      "tech_area_unit_conversion": {
                        "label": "If using a local area unit, indicate conversion factor to one hectare",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_162": {
                    "label": "",
                    "children": {
                      "tech_input_perunit_unit": {
                        "label": "Specify unit",
                        "value": ""
                      },
                      "tech_input_perunit_volume": {
                        "label": "Specify volume, length, etc. (if relevant)",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_164": {
                    "label": "",
                    "children": {
                      "tech_input_dollar": {
                        "label": "Specify currency used for cost calculations",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Specify currency used for cost calculations",
                            "values": [
                              "US Dollars"
                            ],
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_input_national_currency": {
                        "label": "other/ national currency (specify)",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "other/ national currency (specify)",
                            "value": None,
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_input_exchange_rate": {
                        "label": "Indicate exchange rate from USD to local currency (if relevant): 1 USD =",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Indicate exchange rate from USD to local currency (if relevant): 1 USD =",
                            "value": None,
                            "decimals": None,
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_input_average_wage": {
                        "label": "Indicate average wage cost of hired labour per day",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Indicate average wage cost of hired labour per day",
                            "value": None
                          }
                        ]
                      }
                    }
                  }
                }
              },
              "tech__4__4": {
                "label": "Establishment activities",
                "children": {
                  "tech_qg_165": {
                    "label": "",
                    "children": {
                      "tech_est_activity": {
                        "label": "Activity",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Activity",
                            "value": "Demarcation of the contour lines using A frame and Lime",
                            "template": "raw"
                          },
                          {
                            "additional_translations": {},
                            "key": "Activity",
                            "value": "Excavation of the trenches  and construction of the soil bunds",
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_est_type": {
                        "label": "Type of measure",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Type of measure",
                            "value": "Structural",
                            "template": "raw"
                          },
                          {
                            "additional_translations": {},
                            "key": "Type of measure",
                            "value": "Structural",
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_est_timing": {
                        "label": "Timing",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Timing",
                            "value": None,
                            "template": "raw"
                          },
                          {
                            "additional_translations": {},
                            "key": "Timing",
                            "value": None,
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  },
                  "tech_qg_166": {
                    "label": "",
                    "children": {
                      "tech_est_comments": {
                        "label": "Comments",
                        "value": ""
                      }
                    }
                  }
                }
              },
              "tech__4__5": {
                "label": "Costs and inputs needed for establishment",
                "children": {
                  "tech_qg_42": {
                    "label": "",
                    "children": {
                      "tech_input_est_total_estimation": {
                        "label": "If possible, break down the costs of establishment according to the following table, specifying inputs and costs per input. If you are unable to break down the costs, give an estimation of the total costs of establishing the Technology",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_36": {
                    "label": "Labour",
                    "children": {
                      "tech_input_est_specify": {
                        "label": "Specify input",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Specify input",
                            "value": "Demarcation of the contour lines",
                            "template": "raw"
                          },
                          {
                            "additional_translations": {},
                            "key": "Specify input",
                            "value": "Excavation of the trenches and construction of the soil bunds",
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_input_est_unit": {
                        "label": "Unit",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Unit",
                            "value": "ha",
                            "template": "raw"
                          },
                          {
                            "additional_translations": {},
                            "key": "Unit",
                            "value": "persons/day/ha",
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_input_est_quantity": {
                        "label": "Quantity",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Quantity",
                            "value": 1.0,
                            "decimals": None,
                            "template": "raw"
                          },
                          {
                            "additional_translations": {},
                            "key": "Quantity",
                            "value": 121.0,
                            "decimals": None,
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_input_est_costs": {
                        "label": "Costs per Unit",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Costs per Unit",
                            "value": 92.0,
                            "decimals": 2,
                            "template": "raw"
                          },
                          {
                            "additional_translations": {},
                            "key": "Costs per Unit",
                            "value": 7.0,
                            "decimals": 2,
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_input_est_total_costs_pi": {
                        "label": "Total costs per input",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Total costs per input",
                            "value": 92.0,
                            "decimals": 2,
                            "template": "raw"
                          },
                          {
                            "additional_translations": {},
                            "key": "Total costs per input",
                            "value": 847.0,
                            "decimals": 2,
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_input_est_percentage_costs": {
                        "label": "% of costs borne by land users",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "% of costs borne by land users",
                            "value": None,
                            "decimals": None,
                            "template": "raw"
                          },
                          {
                            "additional_translations": {},
                            "key": "% of costs borne by land users",
                            "value": 10.0,
                            "decimals": None,
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  },
                  "tech_qg_37": {
                    "label": "Equipment",
                    "children": {
                      "tech_input_est_specify": {
                        "label": "Specify input",
                        "value": ""
                      },
                      "tech_input_est_unit": {
                        "label": "Unit",
                        "value": ""
                      },
                      "tech_input_est_quantity": {
                        "label": "Quantity",
                        "value": ""
                      },
                      "tech_input_est_costs": {
                        "label": "Costs per Unit",
                        "value": ""
                      },
                      "tech_input_est_total_costs_pi": {
                        "label": "Total costs per input",
                        "value": ""
                      },
                      "tech_input_est_percentage_costs": {
                        "label": "% of costs borne by land users",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_38": {
                    "label": "Plant material",
                    "children": {
                      "tech_input_est_specify": {
                        "label": "Specify input",
                        "value": ""
                      },
                      "tech_input_est_unit": {
                        "label": "Unit",
                        "value": ""
                      },
                      "tech_input_est_quantity": {
                        "label": "Quantity",
                        "value": ""
                      },
                      "tech_input_est_costs": {
                        "label": "Costs per Unit",
                        "value": ""
                      },
                      "tech_input_est_total_costs_pi": {
                        "label": "Total costs per input",
                        "value": ""
                      },
                      "tech_input_est_percentage_costs": {
                        "label": "% of costs borne by land users",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_218": {
                    "label": "Fertilizers and biocides",
                    "children": {
                      "tech_input_est_specify": {
                        "label": "Specify input",
                        "value": ""
                      },
                      "tech_input_est_unit": {
                        "label": "Unit",
                        "value": ""
                      },
                      "tech_input_est_quantity": {
                        "label": "Quantity",
                        "value": ""
                      },
                      "tech_input_est_costs": {
                        "label": "Costs per Unit",
                        "value": ""
                      },
                      "tech_input_est_total_costs_pi": {
                        "label": "Total costs per input",
                        "value": ""
                      },
                      "tech_input_est_percentage_costs": {
                        "label": "% of costs borne by land users",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_39": {
                    "label": "Construction material",
                    "children": {
                      "tech_input_est_specify": {
                        "label": "Specify input",
                        "value": ""
                      },
                      "tech_input_est_unit": {
                        "label": "Unit",
                        "value": ""
                      },
                      "tech_input_est_quantity": {
                        "label": "Quantity",
                        "value": ""
                      },
                      "tech_input_est_costs": {
                        "label": "Costs per Unit",
                        "value": ""
                      },
                      "tech_input_est_total_costs_pi": {
                        "label": "Total costs per input",
                        "value": ""
                      },
                      "tech_input_est_percentage_costs": {
                        "label": "% of costs borne by land users",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_40": {
                    "label": "Other",
                    "children": {
                      "tech_input_est_specify": {
                        "label": "Specify input",
                        "value": ""
                      },
                      "tech_input_est_unit": {
                        "label": "Unit",
                        "value": ""
                      },
                      "tech_input_est_quantity": {
                        "label": "Quantity",
                        "value": ""
                      },
                      "tech_input_est_costs": {
                        "label": "Costs per Unit",
                        "value": ""
                      },
                      "tech_input_est_total_costs_pi": {
                        "label": "Total costs per input",
                        "value": ""
                      },
                      "tech_input_est_percentage_costs": {
                        "label": "% of costs borne by land users",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_222": {
                    "label": "",
                    "children": {
                      "tech_input_est_total_costs": {
                        "label": "Total costs for establishment of the Technology",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Total costs for establishment of the Technology",
                            "value": 939.0,
                            "decimals": 2,
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  },
                  "tech_qg_93": {
                    "label": "",
                    "children": {
                      "tech_input_est_remaining_costs": {
                        "label": "If land user bore less than 100% of costs, indicate who covered the remaining costs",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "If land user bore less than 100% of costs, indicate who covered the remaining costs",
                            "value": None,
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_input_est_comments": {
                        "label": "Comments",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Comments",
                            "value": "Duration of establishment phase: 10 month(s)",
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  }
                }
              },
              "tech__4__6": {
                "label": "Maintenance/ recurrent activities",
                "children": {
                  "tech_qg_43": {
                    "label": "",
                    "children": {
                      "tech_maint_activity": {
                        "label": "Activity",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Activity",
                            "value": "No maintenance costs so far for CRS.",
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_maint_type": {
                        "label": "Type of measure",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Type of measure",
                            "value": "Structural",
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_maint_timing": {
                        "label": "Timing/ frequency",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Timing/ frequency",
                            "value": None,
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  },
                  "tech_qg_44": {
                    "label": "",
                    "children": {
                      "tech_maint_comments": {
                        "label": "Comments",
                        "value": ""
                      }
                    }
                  }
                }
              },
              "tech__4__7": {
                "label": "Costs and inputs needed for maintenance/ recurrent activities (per year)",
                "children": {
                  "tech_qg_50": {
                    "label": "",
                    "children": {
                      "tech_input_maint_total_estimation": {
                        "label": "If possible, break down the costs of maintenance according to the following table, specifying inputs and costs per input. If you are unable to break down the costs, give an estimation of the total costs of maintaining the Technology",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_45": {
                    "label": "Labour",
                    "children": {
                      "tech_input_maint_specify": {
                        "label": "Specify input",
                        "value": ""
                      },
                      "tech_input_maint_unit": {
                        "label": "Unit",
                        "value": ""
                      },
                      "tech_input_maint_quantity": {
                        "label": "Quantity",
                        "value": ""
                      },
                      "tech_input_maint_costs": {
                        "label": "Costs per Unit",
                        "value": ""
                      },
                      "tech_input_maint_total_costs_pi": {
                        "label": "Total costs per input",
                        "value": ""
                      },
                      "tech_input_maint_percentage_costs": {
                        "label": "% of costs borne by land users",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_46": {
                    "label": "Equipment",
                    "children": {
                      "tech_input_maint_specify": {
                        "label": "Specify input",
                        "value": ""
                      },
                      "tech_input_maint_unit": {
                        "label": "Unit",
                        "value": ""
                      },
                      "tech_input_maint_quantity": {
                        "label": "Quantity",
                        "value": ""
                      },
                      "tech_input_maint_costs": {
                        "label": "Costs per Unit",
                        "value": ""
                      },
                      "tech_input_maint_total_costs_pi": {
                        "label": "Total costs per input",
                        "value": ""
                      },
                      "tech_input_maint_percentage_costs": {
                        "label": "% of costs borne by land users",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_47": {
                    "label": "Plant material",
                    "children": {
                      "tech_input_maint_specify": {
                        "label": "Specify input",
                        "value": ""
                      },
                      "tech_input_maint_unit": {
                        "label": "Unit",
                        "value": ""
                      },
                      "tech_input_maint_quantity": {
                        "label": "Quantity",
                        "value": ""
                      },
                      "tech_input_maint_costs": {
                        "label": "Costs per Unit",
                        "value": ""
                      },
                      "tech_input_maint_total_costs_pi": {
                        "label": "Total costs per input",
                        "value": ""
                      },
                      "tech_input_maint_percentage_costs": {
                        "label": "% of costs borne by land users",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_219": {
                    "label": "Fertilizers and biocides",
                    "children": {
                      "tech_input_maint_specify": {
                        "label": "Specify input",
                        "value": ""
                      },
                      "tech_input_maint_unit": {
                        "label": "Unit",
                        "value": ""
                      },
                      "tech_input_maint_quantity": {
                        "label": "Quantity",
                        "value": ""
                      },
                      "tech_input_maint_costs": {
                        "label": "Costs per Unit",
                        "value": ""
                      },
                      "tech_input_maint_total_costs_pi": {
                        "label": "Total costs per input",
                        "value": ""
                      },
                      "tech_input_maint_percentage_costs": {
                        "label": "% of costs borne by land users",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_48": {
                    "label": "Construction material",
                    "children": {
                      "tech_input_maint_specify": {
                        "label": "Specify input",
                        "value": ""
                      },
                      "tech_input_maint_unit": {
                        "label": "Unit",
                        "value": ""
                      },
                      "tech_input_maint_quantity": {
                        "label": "Quantity",
                        "value": ""
                      },
                      "tech_input_maint_costs": {
                        "label": "Costs per Unit",
                        "value": ""
                      },
                      "tech_input_maint_total_costs_pi": {
                        "label": "Total costs per input",
                        "value": ""
                      },
                      "tech_input_maint_percentage_costs": {
                        "label": "% of costs borne by land users",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_49": {
                    "label": "Other",
                    "children": {
                      "tech_input_maint_specify": {
                        "label": "Specify input",
                        "value": ""
                      },
                      "tech_input_maint_unit": {
                        "label": "Unit",
                        "value": ""
                      },
                      "tech_input_maint_quantity": {
                        "label": "Quantity",
                        "value": ""
                      },
                      "tech_input_maint_costs": {
                        "label": "Costs per Unit",
                        "value": ""
                      },
                      "tech_input_maint_total_costs_pi": {
                        "label": "Total costs per input",
                        "value": ""
                      },
                      "tech_input_maint_percentage_costs": {
                        "label": "% of costs borne by land users",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_223": {
                    "label": "",
                    "children": {
                      "tech_input_maint_total_costs": {
                        "label": "Total costs for maintenance of the Technology",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_52": {
                    "label": "",
                    "children": {
                      "tech_input_maint_remaining_costs": {
                        "label": "If land user bore less than 100% of costs, indicate who covered the remaining costs",
                        "value": ""
                      },
                      "tech_input_maint_comments": {
                        "label": "Comments",
                        "value": ""
                      }
                    }
                  }
                }
              },
              "tech__4__8": {
                "label": "Most important factors affecting the costs",
                "children": {
                  "tech_qg_95": {
                    "label": "",
                    "children": {
                      "tech_input_determinate_factors": {
                        "label": "Describe the most determinate factors affecting the costs",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Describe the most determinate factors affecting the costs",
                            "value": "The establishment duration of the Contour Trench Bund was 10 months.",
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  }
                }
              }
            }
          },
          "tech__5": {
            "label": "Natural and human environment",
            "children": {
              "tech__5__1": {
                "label": "Climate",
                "children": {
                  "tech_qg_54": {
                    "label": "Annual rainfall",
                    "children": {
                      "tech_rainfall": {
                        "label": "Average annual rainfall",
                        "value": [
                          {
                            "layout": "stacked",
                            "template": "raw",
                            "label_position": "none",
                            "additional_translations": {},
                            "key": "Average annual rainfall",
                            "values": [
                              "251-500 mm"
                            ],
                            "all_values": [
                              [
                                1,
                                "< 250 mm"
                              ],
                              [
                                5,
                                "251-500 mm"
                              ],
                              [
                                1,
                                "501-750 mm"
                              ],
                              [
                                1,
                                "751-1,000 mm"
                              ],
                              [
                                1,
                                "1,001-1,500 mm"
                              ],
                              [
                                1,
                                "1,501-2,000 mm"
                              ],
                              [
                                1,
                                "2,001-3,000 mm"
                              ],
                              [
                                1,
                                "3,001-4,000 mm"
                              ],
                              [
                                1,
                                "> 4,000 mm"
                              ]
                            ],
                            "label_text_direction": None
                          }
                        ]
                      },
                      "tech_rainfall_annual": {
                        "label": "Specify average annual rainfall (if known), in mm",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Specify average annual rainfall (if known), in mm",
                            "value": None,
                            "decimals": 2,
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_rainfall_specifications": {
                        "label": "Specifications/ comments on rainfall",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Specifications/ comments on rainfall",
                            "value": None,
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_rainfall_meteostation": {
                        "label": "Indicate the name of the reference meteorological station considered",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Indicate the name of the reference meteorological station considered",
                            "value": None,
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  },
                  "tech_qg_55": {
                    "label": "Agro-climatic zone",
                    "children": {
                      "tech_agroclimatic_zone": {
                        "label": "Agro-climatic zone",
                        "value": [
                          {
                            "label_position": "none",
                            "additional_translations": {},
                            "key": "Agro-climatic zone",
                            "values": [
                              "semi-arid"
                            ],
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_agroclimatic_zone_specifications": {
                        "label": "Specifications/ comments on climate",
                        "value": [
                          {
                            "label_position": "none",
                            "additional_translations": {},
                            "key": "Specifications/ comments on climate",
                            "value": "Thermal climate class: Temperate",
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  }
                }
              },
              "tech__5__2": {
                "label": "Topography",
                "children": {
                  "tech_qg_56": {
                    "label": "",
                    "children": {
                      "tech_slopes": {
                        "label": "Slopes on average",
                        "value": [
                          {
                            "layout": "stacked",
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Slopes on average",
                            "values": [
                              "rolling (11-15%)",
                              "hilly (16-30%)"
                            ],
                            "all_values": [
                              [
                                1,
                                "flat (0-2%)"
                              ],
                              [
                                1,
                                "gentle (3-5%)"
                              ],
                              [
                                1,
                                "moderate (6-10%)"
                              ],
                              [
                                5,
                                "rolling (11-15%)"
                              ],
                              [
                                5,
                                "hilly (16-30%)"
                              ],
                              [
                                1,
                                "steep (31-60%)"
                              ],
                              [
                                1,
                                "very steep (>60%)"
                              ]
                            ],
                            "label_text_direction": None
                          }
                        ]
                      },
                      "tech_landforms": {
                        "label": "Landforms",
                        "value": [
                          {
                            "layout": "stacked",
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Landforms",
                            "values": [
                              "mountain slopes",
                              "hill slopes"
                            ],
                            "all_values": [
                              [
                                1,
                                "plateau/plains"
                              ],
                              [
                                1,
                                "ridges"
                              ],
                              [
                                5,
                                "mountain slopes"
                              ],
                              [
                                5,
                                "hill slopes"
                              ],
                              [
                                1,
                                "footslopes"
                              ],
                              [
                                1,
                                "valley floors"
                              ]
                            ],
                            "label_text_direction": None
                          }
                        ]
                      },
                      "tech_altitudinalzone": {
                        "label": "Altitudinal zone",
                        "value": [
                          {
                            "layout": "stacked",
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Altitudinal zone",
                            "values": [
                              "1,501-2,000 m a.s.l.",
                              "2,501-3,000 m a.s.l."
                            ],
                            "all_values": [
                              [
                                1,
                                "0-100 m a.s.l."
                              ],
                              [
                                1,
                                "101-500 m a.s.l."
                              ],
                              [
                                1,
                                "501-1,000 m a.s.l."
                              ],
                              [
                                1,
                                "1,001-1,500 m a.s.l."
                              ],
                              [
                                5,
                                "1,501-2,000 m a.s.l."
                              ],
                              [
                                1,
                                "2,001-2,500 m a.s.l."
                              ],
                              [
                                5,
                                "2,501-3,000 m a.s.l."
                              ],
                              [
                                1,
                                "3,001-4,000 m a.s.l."
                              ],
                              [
                                1,
                                "> 4,000 m a.s.l."
                              ]
                            ],
                            "label_text_direction": None
                          }
                        ]
                      }
                    }
                  },
                  "tech_qg_57": {
                    "label": "",
                    "children": {
                      "tech_convex_concave": {
                        "label": "Indicate if the Technology is specifically applied in",
                        "value": ""
                      },
                      "tech_topography_comments": {
                        "label": "Comments and further specifications on topography",
                        "value": ""
                      }
                    }
                  }
                }
              },
              "tech__5__3": {
                "label": "Soils",
                "children": {
                  "tech_qg_58": {
                    "label": "",
                    "children": {
                      "tech_soil_depth": {
                        "label": "Soil depth on average",
                        "value": [
                          {
                            "layout": "stacked",
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Soil depth on average",
                            "values": [
                              "shallow (21-50 cm)"
                            ],
                            "all_values": [
                              [
                                1,
                                "very shallow (0-20 cm)"
                              ],
                              [
                                5,
                                "shallow (21-50 cm)"
                              ],
                              [
                                1,
                                "moderately deep (51-80 cm)"
                              ],
                              [
                                1,
                                "deep (81-120 cm)"
                              ],
                              [
                                1,
                                "very deep (> 120 cm)"
                              ]
                            ],
                            "label_text_direction": None
                          }
                        ]
                      },
                      "tech_soil_texture_topsoil": {
                        "label": "Soil texture (topsoil)",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Soil texture (topsoil)",
                            "values": [
                              "coarse/ light (sandy)",
                              "medium (loamy, silty)"
                            ],
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_soil_texture_20cm": {
                        "label": "Soil texture (> 20 cm below surface)",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Soil texture (> 20 cm below surface)",
                            "values": [],
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_topsoil_organic": {
                        "label": "Topsoil organic matter",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Topsoil organic matter",
                            "values": [
                              "low (<1%)"
                            ],
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  },
                  "tech_qg_59": {
                    "label": "",
                    "children": {
                      "tech_soil_comments": {
                        "label": "If available, attach full soil description or specify the available information, e.g. soil type, soil PH/ acidity, Cation Exchange Capacity, nitrogen, salinity etc.",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "If available, attach full soil description or specify the available information, e.g. soil type, soil PH/ acidity, Cation Exchange Capacity, nitrogen, salinity etc.",
                            "value": "Soil fertility is low - medium\r\n\r\nSoil drainage / infiltration is medium\r\n\r\nSoil water storage capacity is medium",
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  }
                }
              },
              "tech__5__4": {
                "label": "Water availability and quality",
                "children": {
                  "tech_qg_60": {
                    "label": "",
                    "children": {
                      "tech_groundwater": {
                        "label": "Ground water table",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Ground water table",
                            "values": [
                              "5-50 m"
                            ]
                          }
                        ]
                      },
                      "tech_surfacewater": {
                        "label": "Availability of surface water",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Availability of surface water",
                            "values": [
                              "poor/ none"
                            ]
                          }
                        ]
                      },
                      "tech_waterquality": {
                        "label": "Water quality (untreated)",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Water quality (untreated)",
                            "values": [
                              "good drinking water"
                            ]
                          }
                        ]
                      }
                    }
                  },
                  "tech_qg_61": {
                    "label": "",
                    "children": {
                      "tech_salinization": {
                        "label": "Is water salinity a problem?",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_62": {
                    "label": "",
                    "children": {
                      "tech_salinization_specification": {
                        "label": "Specify",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_63": {
                    "label": "",
                    "children": {
                      "tech_flooding": {
                        "label": "Is flooding of the area occurring?",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_64": {
                    "label": "",
                    "children": {
                      "tech_flooding_regularity": {
                        "label": "Regularity",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_65": {
                    "label": "",
                    "children": {
                      "tech_water_comments": {
                        "label": "Comments and further specifications on water quality and quantity",
                        "value": ""
                      }
                    }
                  }
                }
              },
              "tech__5__5": {
                "label": "Biodiversity",
                "children": {
                  "tech_qg_66": {
                    "label": "",
                    "children": {
                      "tech_speciesdiversity": {
                        "label": "Species diversity",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Species diversity",
                            "values": [
                              "medium"
                            ],
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_habitatdiversity": {
                        "label": "Habitat diversity",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Habitat diversity",
                            "values": [],
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  },
                  "tech_qg_67": {
                    "label": "",
                    "children": {
                      "tech_biodiversity_comments": {
                        "label": "Comments and further specifications on biodiversity",
                        "value": ""
                      }
                    }
                  }
                }
              },
              "tech__5__6": {
                "label": "Characteristics of land users applying the Technology",
                "children": {
                  "tech_qg_71": {
                    "label": "",
                    "children": {
                      "tech_sedentary_nomadic": {
                        "label": "Sedentary or nomadic",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Sedentary or nomadic",
                            "values": [],
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_sedentary_other": {
                        "label": "other (specify)",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "other (specify)",
                            "value": None,
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_market_orientation": {
                        "label": "Market orientation of production system",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Market orientation of production system",
                            "values": [
                              "mixed (subsistence/ commercial"
                            ],
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_offfarm_income": {
                        "label": "Off-farm income",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Off-farm income",
                            "values": [
                              "10-50% of all income"
                            ],
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_wealth": {
                        "label": "Relative level of wealth",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Relative level of wealth",
                            "values": [
                              "poor"
                            ],
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_individuals": {
                        "label": "Individuals or groups",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Individuals or groups",
                            "values": [
                              "groups/ community"
                            ],
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_mechanisation": {
                        "label": "Level of mechanization",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Level of mechanization",
                            "values": [],
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_gender": {
                        "label": "Gender",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Gender",
                            "values": [
                              "men"
                            ],
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_age_landusers": {
                        "label": "Age of land users",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Age of land users",
                            "values": [],
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  },
                  "tech_qg_77": {
                    "label": "",
                    "children": {
                      "tech_landuser_comments": {
                        "label": "Indicate other relevant characteristics of the land users",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Indicate other relevant characteristics of the land users",
                            "value": "Difference in the involvement of women and men: Workload does not give chance to women to work on the mountains.\r\n\r\nPopulation density: < 10 persons/km2\r\n\r\nAnnual population growth: 2% - 3%\r\n\r\n50% of the land users are poor.\r\n\r\nOff-farm income specification: Busy with carpentry and migrate for work.",
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  }
                }
              },
              "tech__5__7": {
                "label": "Average area of land owned or leased by land users applying the Technology",
                "children": {
                  "tech_qg_72": {
                    "label": "",
                    "children": {
                      "tech_land_size": {
                        "label": "Land size per household/farm unit applying the technology",
                        "value": [
                          {
                            "layout": "stacked",
                            "template": "raw",
                            "label_position": "none",
                            "additional_translations": {},
                            "key": "Land size per household/farm unit applying the technology",
                            "values": [
                              "2-5 ha"
                            ],
                            "all_values": [
                              [
                                1,
                                "< 0.5 ha"
                              ],
                              [
                                1,
                                "0.5-1 ha"
                              ],
                              [
                                1,
                                "1-2 ha"
                              ],
                              [
                                5,
                                "2-5 ha"
                              ],
                              [
                                1,
                                "5-15 ha"
                              ],
                              [
                                1,
                                "15-50 ha"
                              ],
                              [
                                1,
                                "50-100 ha"
                              ],
                              [
                                1,
                                "100-500 ha"
                              ],
                              [
                                1,
                                "500-1,000 ha"
                              ],
                              [
                                1,
                                "1,000-10,000 ha"
                              ],
                              [
                                1,
                                "> 10,000 ha"
                              ]
                            ],
                            "label_text_direction": None
                          }
                        ]
                      },
                      "tech_land_size_relative": {
                        "label": "Is this considered small-, medium- or large-scale (referring to local context)?",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Is this considered small-, medium- or large-scale (referring to local context)?",
                            "values": [
                              "medium-scale"
                            ],
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_land_comments": {
                        "label": "Comments",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Comments",
                            "value": None,
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  }
                }
              },
              "tech__5__8": {
                "label": "Land ownership, land use rights, and water use rights",
                "children": {
                  "tech_qg_73": {
                    "label": "None",
                    "children": {
                      "tech_ownership": {
                        "label": "Land ownership",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Land ownership",
                            "values": [
                              "communal/ village"
                            ],
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_ownership_other": {
                        "label": "other (specify)",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "other (specify)",
                            "value": None
                          }
                        ]
                      },
                      "tech_landuserights": {
                        "label": "Land use rights",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Land use rights",
                            "values": [
                              "communal (organized)"
                            ],
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_landrights_other": {
                        "label": "other (specify)",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "other (specify)",
                            "value": None
                          }
                        ]
                      },
                      "tech_wateruserights": {
                        "label": "Water use rights",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Water use rights",
                            "values": [
                              "open access (unorganized)"
                            ],
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_waterrights_other": {
                        "label": "other (specify)",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "other (specify)",
                            "value": None
                          }
                        ]
                      }
                    }
                  },
                  "tech_qg_75": {
                    "label": "",
                    "children": {
                      "tech_ownership_comments": {
                        "label": "Comments",
                        "value": ""
                      }
                    }
                  }
                }
              },
              "tech__5__9": {
                "label": "Access to services and infrastructure",
                "children": {
                  "tech_qg_226": {
                    "label": "",
                    "children": {
                      "tech_access_health": {
                        "label": "health",
                        "value": [
                          {
                            "layout": "stacked",
                            "template": "raw",
                            "additional_translations": {
                              "label_left": None,
                              "label_right": None
                            },
                            "key": "health",
                            "value": "poor",
                            "level": 0,
                            "all_values": [
                              [
                                5,
                                "poor"
                              ],
                              [
                                1,
                                "moderate"
                              ],
                              [
                                1,
                                "good"
                              ]
                            ],
                            "label_text_direction": None
                          }
                        ]
                      },
                      "tech_access_education": {
                        "label": "education",
                        "value": [
                          {
                            "layout": "stacked",
                            "template": "raw",
                            "additional_translations": {
                              "label_left": None,
                              "label_right": None
                            },
                            "key": "education",
                            "value": "moderate",
                            "level": 2,
                            "all_values": [
                              [
                                1,
                                "poor"
                              ],
                              [
                                5,
                                "moderate"
                              ],
                              [
                                1,
                                "good"
                              ]
                            ],
                            "label_text_direction": None
                          }
                        ]
                      },
                      "tech_access_techassistance": {
                        "label": "technical assistance",
                        "value": [
                          {
                            "layout": "stacked",
                            "template": "raw",
                            "additional_translations": {
                              "label_left": None,
                              "label_right": None
                            },
                            "key": "technical assistance",
                            "value": "moderate",
                            "level": 2,
                            "all_values": [
                              [
                                1,
                                "poor"
                              ],
                              [
                                5,
                                "moderate"
                              ],
                              [
                                1,
                                "good"
                              ]
                            ],
                            "label_text_direction": None
                          }
                        ]
                      },
                      "tech_access_employment": {
                        "label": "employment (e.g. off-farm)",
                        "value": [
                          {
                            "layout": "stacked",
                            "template": "raw",
                            "additional_translations": {
                              "label_left": None,
                              "label_right": None
                            },
                            "key": "employment (e.g. off-farm)",
                            "value": "poor",
                            "level": 0,
                            "all_values": [
                              [
                                5,
                                "poor"
                              ],
                              [
                                1,
                                "moderate"
                              ],
                              [
                                1,
                                "good"
                              ]
                            ],
                            "label_text_direction": None
                          }
                        ]
                      },
                      "tech_access_markets": {
                        "label": "markets",
                        "value": [
                          {
                            "layout": "stacked",
                            "template": "raw",
                            "additional_translations": {
                              "label_left": None,
                              "label_right": None
                            },
                            "key": "markets",
                            "value": "poor",
                            "level": 0,
                            "all_values": [
                              [
                                5,
                                "poor"
                              ],
                              [
                                1,
                                "moderate"
                              ],
                              [
                                1,
                                "good"
                              ]
                            ],
                            "label_text_direction": None
                          }
                        ]
                      },
                      "tech_access_energy": {
                        "label": "energy",
                        "value": [
                          {
                            "layout": "stacked",
                            "template": "raw",
                            "additional_translations": {
                              "label_left": None,
                              "label_right": None
                            },
                            "key": "energy",
                            "value": "poor",
                            "level": 0,
                            "all_values": [
                              [
                                5,
                                "poor"
                              ],
                              [
                                1,
                                "moderate"
                              ],
                              [
                                1,
                                "good"
                              ]
                            ],
                            "label_text_direction": None
                          }
                        ]
                      },
                      "tech_access_roads": {
                        "label": "roads and transport",
                        "value": [
                          {
                            "layout": "stacked",
                            "template": "raw",
                            "additional_translations": {
                              "label_left": None,
                              "label_right": None
                            },
                            "key": "roads and transport",
                            "value": "moderate",
                            "level": 2,
                            "all_values": [
                              [
                                1,
                                "poor"
                              ],
                              [
                                5,
                                "moderate"
                              ],
                              [
                                1,
                                "good"
                              ]
                            ],
                            "label_text_direction": None
                          }
                        ]
                      },
                      "tech_access_water": {
                        "label": "drinking water and sanitation",
                        "value": [
                          {
                            "layout": "stacked",
                            "template": "raw",
                            "additional_translations": {
                              "label_left": None,
                              "label_right": None
                            },
                            "key": "drinking water and sanitation",
                            "value": "moderate",
                            "level": 2,
                            "all_values": [
                              [
                                1,
                                "poor"
                              ],
                              [
                                5,
                                "moderate"
                              ],
                              [
                                1,
                                "good"
                              ]
                            ],
                            "label_text_direction": None
                          }
                        ]
                      },
                      "tech_access_financial": {
                        "label": "financial services",
                        "value": [
                          {
                            "layout": "stacked",
                            "template": "raw",
                            "additional_translations": {
                              "label_left": None,
                              "label_right": None
                            },
                            "key": "financial services",
                            "value": "poor",
                            "level": 0,
                            "all_values": [
                              [
                                5,
                                "poor"
                              ],
                              [
                                1,
                                "moderate"
                              ],
                              [
                                1,
                                "good"
                              ]
                            ],
                            "label_text_direction": None
                          }
                        ]
                      }
                    }
                  },
                  "tech_qg_227": {
                    "label": "",
                    "children": {
                      "tech_access_other_specify": {
                        "label": "other (specify)",
                        "value": ""
                      },
                      "tech_access_other_measure": {
                        "label": "other (specify)",
                        "value": ""
                      }
                    }
                  }
                }
              }
            }
          },
          "tech__6": {
            "label": "Impacts and concluding statements",
            "children": {
              "tech__6__1": {
                "label": "On-site impacts the Technology has shown",
                "children": {
                  "tech__8__1__socioeconomic": {
                    "label": "Socio-economic impacts",
                    "children": {
                      "tech__8__1__socioeconomic_production": {
                        "label": "Production",
                        "children": {
                          "tech_qg_76": {
                            "label": "crop production",
                            "children": {
                              "tech_impacts_cropproduction": {
                                "label": "Crop production",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_78": {
                            "label": "crop quality",
                            "children": {
                              "tech_impacts_cropquality": {
                                "label": "crop quality",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_79": {
                            "label": "fodder production",
                            "children": {
                              "tech_impacts_fodderproduction": {
                                "label": "fodder production",
                                "value": [
                                  {
                                    "layout": "stacked",
                                    "template": "raw",
                                    "additional_translations": {
                                      "label_left": "decreased",
                                      "label_right": "increased"
                                    },
                                    "key": "fodder production",
                                    "value": "2",
                                    "level": 4,
                                    "all_values": [
                                      [
                                        1,
                                        "-3"
                                      ],
                                      [
                                        1,
                                        "-2"
                                      ],
                                      [
                                        1,
                                        "-1"
                                      ],
                                      [
                                        1,
                                        "0"
                                      ],
                                      [
                                        1,
                                        "1"
                                      ],
                                      [
                                        5,
                                        "2"
                                      ],
                                      [
                                        1,
                                        "3"
                                      ]
                                    ],
                                    "label_text_direction": None
                                  }
                                ]
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Quantity before SLM",
                                    "value": None
                                  }
                                ]
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Quantity after SLM",
                                    "value": None
                                  }
                                ]
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Comments/ specify",
                                    "value": "Due to better soil moisture"
                                  }
                                ]
                              }
                            }
                          },
                          "tech_qg_80": {
                            "label": "fodder quality",
                            "children": {
                              "tech_impacts_fodderquality": {
                                "label": "fodder quality",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_81": {
                            "label": "animal production",
                            "children": {
                              "tech_impacts_animalproduction": {
                                "label": "animal production",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_82": {
                            "label": "wood production",
                            "children": {
                              "tech_impacts_woodproduction": {
                                "label": "wood production",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_83": {
                            "label": "forest/ woodland quality",
                            "children": {
                              "tech_impacts_forestquality": {
                                "label": "forest/ woodland quality",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_84": {
                            "label": "non-wood forest production",
                            "children": {
                              "tech_impacts_nonwoodforestproduction": {
                                "label": "non-wood forest production",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_85": {
                            "label": "risk of production failure",
                            "children": {
                              "tech_impacts_productionfailure": {
                                "label": "risk of production failure",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_86": {
                            "label": "product diversity",
                            "children": {
                              "tech_impacts_productdiversity": {
                                "label": "product diversity",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_87": {
                            "label": "production area",
                            "children": {
                              "tech_impacts_productionarea": {
                                "label": "production area (new land under cultivation/ use)",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_88": {
                            "label": "land management",
                            "children": {
                              "tech_impacts_landmanagement": {
                                "label": "land management",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_90": {
                            "label": "energy generation",
                            "children": {
                              "tech_impacts_energygeneration": {
                                "label": "energy generation (e.g. hydro, bio)",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          }
                        }
                      },
                      "tech__8__1__socioeconomic_water": {
                        "label": "Water availability and quality",
                        "children": {
                          "tech_qg_91": {
                            "label": "drinking water availability",
                            "children": {
                              "tech_impacts_drinkingwateravailability": {
                                "label": "drinking water availability",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_97": {
                            "label": "drinking water quality",
                            "children": {
                              "tech_impacts_drinkingwaterquality": {
                                "label": "drinking water quality",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_98": {
                            "label": "water availability for livestock",
                            "children": {
                              "tech_impacts_livestockwateravailability": {
                                "label": "water availability for livestock",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_99": {
                            "label": "water quality for livestock",
                            "children": {
                              "tech_impacts_livestockwaterquality": {
                                "label": "water quality for livestock",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_100": {
                            "label": "irrigation water availability",
                            "children": {
                              "tech_impacts_irrigationwateravailability": {
                                "label": "irrigation water availability",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_101": {
                            "label": "irrigation water quality",
                            "children": {
                              "tech_impacts_irrigationwaterquality": {
                                "label": "irrigation water quality",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_102": {
                            "label": "demand for irrigation water",
                            "children": {
                              "tech_impacts_demandirrigationwater": {
                                "label": "demand for irrigation water",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          }
                        }
                      },
                      "tech__8__1__socioeconomic_income": {
                        "label": "Income and costs",
                        "children": {
                          "tech_qg_103": {
                            "label": "expenses on agricultural inputs",
                            "children": {
                              "tech_impacts_expenses": {
                                "label": "expenses on agricultural inputs",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_104": {
                            "label": "farm income",
                            "children": {
                              "tech_impacts_farmincome": {
                                "label": "farm income",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_105": {
                            "label": "diversity of income sources",
                            "children": {
                              "tech_impacts_diversityincome": {
                                "label": "diversity of income sources",
                                "value": [
                                  {
                                    "layout": "stacked",
                                    "template": "raw",
                                    "additional_translations": {
                                      "label_left": "decreased",
                                      "label_right": "increased"
                                    },
                                    "key": "diversity of income sources",
                                    "value": "2",
                                    "level": 4,
                                    "all_values": [
                                      [
                                        1,
                                        "-3"
                                      ],
                                      [
                                        1,
                                        "-2"
                                      ],
                                      [
                                        1,
                                        "-1"
                                      ],
                                      [
                                        1,
                                        "0"
                                      ],
                                      [
                                        1,
                                        "1"
                                      ],
                                      [
                                        5,
                                        "2"
                                      ],
                                      [
                                        1,
                                        "3"
                                      ]
                                    ],
                                    "label_text_direction": None
                                  }
                                ]
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Quantity before SLM",
                                    "value": None
                                  }
                                ]
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Quantity after SLM",
                                    "value": None
                                  }
                                ]
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Comments/ specify",
                                    "value": None
                                  }
                                ]
                              }
                            }
                          },
                          "tech_qg_106": {
                            "label": "economic disparities",
                            "children": {
                              "tech_impacts_economicdisparities": {
                                "label": "economic disparities",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_107": {
                            "label": "workload",
                            "children": {
                              "tech_impacts_workload": {
                                "label": "workload",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          }
                        }
                      },
                      "tech__8__1__socioeconomic_other": {
                        "label": "Other socio-economic impacts",
                        "children": {
                          "tech_qg_186": {
                            "label": "other",
                            "children": {
                              "tech_impacts_other_specify": {
                                "label": "Specify",
                                "value": ""
                              },
                              "tech_impacts_other_labelleft": {
                                "label": "[Label left]",
                                "value": ""
                              },
                              "tech_impacts_other_measure": {
                                "label": "[Measure]",
                                "value": ""
                              },
                              "tech_impacts_other_labelright": {
                                "label": "[Label right]",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          }
                        }
                      }
                    }
                  },
                  "tech__8__1__sociocultural": {
                    "label": "Socio-cultural impacts",
                    "children": {
                      "tech__8__1__sociocultural": {
                        "label": "Socio-cultural impacts",
                        "children": {
                          "tech_qg_108": {
                            "label": "food security/ self-sufficiency",
                            "children": {
                              "tech_impacts_foodsecurity": {
                                "label": "food security/ self-sufficiency",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_109": {
                            "label": "health situation",
                            "children": {
                              "tech_impacts_health": {
                                "label": "health situation",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_110": {
                            "label": "land use/ water rights",
                            "children": {
                              "tech_impacts_landuse": {
                                "label": "land use/ water rights",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_111": {
                            "label": "cultural opportunities",
                            "children": {
                              "tech_impacts_cultural": {
                                "label": "cultural opportunities (eg spiritual, aesthetic, others)",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_112": {
                            "label": "recreational opportunities",
                            "children": {
                              "tech_impacts_recreational": {
                                "label": "recreational opportunities",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_113": {
                            "label": "community institutions",
                            "children": {
                              "tech_impacts_community": {
                                "label": "community institutions",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_114": {
                            "label": "national institutions",
                            "children": {
                              "tech_impacts_national": {
                                "label": "national institutions",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_115": {
                            "label": "SLM/ land degradation knowledge",
                            "children": {
                              "tech_impacts_slmknowledge": {
                                "label": "SLM/ land degradation knowledge",
                                "value": [
                                  {
                                    "layout": "stacked",
                                    "template": "raw",
                                    "additional_translations": {
                                      "label_left": "reduced",
                                      "label_right": "improved"
                                    },
                                    "key": "SLM/ land degradation knowledge",
                                    "value": "2",
                                    "level": 4,
                                    "all_values": [
                                      [
                                        1,
                                        "-3"
                                      ],
                                      [
                                        1,
                                        "-2"
                                      ],
                                      [
                                        1,
                                        "-1"
                                      ],
                                      [
                                        1,
                                        "0"
                                      ],
                                      [
                                        1,
                                        "1"
                                      ],
                                      [
                                        5,
                                        "2"
                                      ],
                                      [
                                        1,
                                        "3"
                                      ]
                                    ],
                                    "label_text_direction": None
                                  }
                                ]
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Quantity before SLM",
                                    "value": None
                                  }
                                ]
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Quantity after SLM",
                                    "value": None
                                  }
                                ]
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Comments/ specify",
                                    "value": None
                                  }
                                ]
                              }
                            }
                          },
                          "tech_qg_116": {
                            "label": "conflict mitigation",
                            "children": {
                              "tech_impacts_conflictmitigation": {
                                "label": "conflict mitigation",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_117": {
                            "label": "situation of socially and economically disadvantaged groups",
                            "children": {
                              "tech_impacts_situationdisadvantaged": {
                                "label": "situation of socially and economically disadvantaged groups (gender, age, status, ehtnicity etc.)",
                                "value": [
                                  {
                                    "layout": "stacked",
                                    "template": "raw",
                                    "additional_translations": {
                                      "label_left": "worsened",
                                      "label_right": "improved"
                                    },
                                    "key": "situation of socially and economically disadvantaged groups (gender, age, status, ehtnicity etc.)",
                                    "value": "2",
                                    "level": 4,
                                    "all_values": [
                                      [
                                        1,
                                        "-3"
                                      ],
                                      [
                                        1,
                                        "-2"
                                      ],
                                      [
                                        1,
                                        "-1"
                                      ],
                                      [
                                        1,
                                        "0"
                                      ],
                                      [
                                        1,
                                        "1"
                                      ],
                                      [
                                        5,
                                        "2"
                                      ],
                                      [
                                        1,
                                        "3"
                                      ]
                                    ],
                                    "label_text_direction": None
                                  }
                                ]
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Quantity before SLM",
                                    "value": None
                                  }
                                ]
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Quantity after SLM",
                                    "value": None
                                  }
                                ]
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Comments/ specify",
                                    "value": None
                                  }
                                ]
                              }
                            }
                          },
                          "tech_qg_187": {
                            "label": "other",
                            "children": {
                              "tech_impacts_other_specify": {
                                "label": "Specify",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Specify",
                                    "value": "livelihood and human well-being"
                                  }
                                ]
                              },
                              "tech_impacts_other_labelleft": {
                                "label": "[Label left]",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "[Label left]",
                                    "value": "reduced"
                                  }
                                ]
                              },
                              "tech_impacts_other_measure": {
                                "label": "[Measure]",
                                "value": [
                                  {
                                    "layout": "stacked",
                                    "template": "raw",
                                    "additional_translations": {
                                      "label_left": None,
                                      "label_right": None
                                    },
                                    "key": "[Measure]",
                                    "value": "2",
                                    "level": 4,
                                    "all_values": [
                                      [
                                        1,
                                        "-3"
                                      ],
                                      [
                                        1,
                                        "-2"
                                      ],
                                      [
                                        1,
                                        "-1"
                                      ],
                                      [
                                        1,
                                        "0"
                                      ],
                                      [
                                        1,
                                        "1"
                                      ],
                                      [
                                        5,
                                        "2"
                                      ],
                                      [
                                        1,
                                        "3"
                                      ]
                                    ],
                                    "label_text_direction": None
                                  }
                                ]
                              },
                              "tech_impacts_other_labelright": {
                                "label": "[Label right]",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "[Label right]",
                                    "value": "improved"
                                  }
                                ]
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Quantity before SLM",
                                    "value": None
                                  }
                                ]
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Quantity after SLM",
                                    "value": None
                                  }
                                ]
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Comments/ specify",
                                    "value": "Due to reduction in flash floods problem and increased access to drinking water, Seasonal job opportunities created through cash for work"
                                  }
                                ]
                              }
                            }
                          }
                        }
                      }
                    }
                  },
                  "tech__8__1__ecological": {
                    "label": "Ecological impacts",
                    "children": {
                      "tech__8__1__ecological_water": {
                        "label": "Water cycle/ runoff",
                        "children": {
                          "tech_qg_118": {
                            "label": "water quantity",
                            "children": {
                              "tech_impacts_waterquantity": {
                                "label": "water quantity",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_119": {
                            "label": "water quality",
                            "children": {
                              "tech_impacts_waterquality": {
                                "label": "water quality",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_120": {
                            "label": "harvesting/ collection of water",
                            "children": {
                              "tech_impacts_harvestingwater": {
                                "label": "harvesting/ collection of water (runoff, dew, snow, etc)",
                                "value": [
                                  {
                                    "layout": "stacked",
                                    "template": "raw",
                                    "additional_translations": {
                                      "label_left": "reduced",
                                      "label_right": "improved"
                                    },
                                    "key": "harvesting/ collection of water (runoff, dew, snow, etc)",
                                    "value": "2",
                                    "level": 4,
                                    "all_values": [
                                      [
                                        1,
                                        "-3"
                                      ],
                                      [
                                        1,
                                        "-2"
                                      ],
                                      [
                                        1,
                                        "-1"
                                      ],
                                      [
                                        1,
                                        "0"
                                      ],
                                      [
                                        1,
                                        "1"
                                      ],
                                      [
                                        5,
                                        "2"
                                      ],
                                      [
                                        1,
                                        "3"
                                      ]
                                    ],
                                    "label_text_direction": None
                                  }
                                ]
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Quantity before SLM",
                                    "value": None
                                  }
                                ]
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Quantity after SLM",
                                    "value": None
                                  }
                                ]
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Comments/ specify",
                                    "value": "of surface run off"
                                  }
                                ]
                              }
                            }
                          },
                          "tech_qg_121": {
                            "label": "surface runoff",
                            "children": {
                              "tech_impacts_surfacerunoff": {
                                "label": "surface runoff",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_122": {
                            "label": "excess water drainage",
                            "children": {
                              "tech_impacts_waterdrainage": {
                                "label": "excess water drainage",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_123": {
                            "label": "groundwater table/ aquifer",
                            "children": {
                              "tech_impacts_groundwater": {
                                "label": "groundwater table/ aquifer",
                                "value": [
                                  {
                                    "layout": "stacked",
                                    "template": "raw",
                                    "additional_translations": {
                                      "label_left": "lowered",
                                      "label_right": "recharge"
                                    },
                                    "key": "groundwater table/ aquifer",
                                    "value": "1",
                                    "level": 3,
                                    "all_values": [
                                      [
                                        1,
                                        "-3"
                                      ],
                                      [
                                        1,
                                        "-2"
                                      ],
                                      [
                                        1,
                                        "-1"
                                      ],
                                      [
                                        1,
                                        "0"
                                      ],
                                      [
                                        5,
                                        "1"
                                      ],
                                      [
                                        1,
                                        "2"
                                      ],
                                      [
                                        1,
                                        "3"
                                      ]
                                    ],
                                    "label_text_direction": None
                                  }
                                ]
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Quantity before SLM",
                                    "value": None
                                  }
                                ]
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Quantity after SLM",
                                    "value": None
                                  }
                                ]
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Comments/ specify",
                                    "value": None
                                  }
                                ]
                              }
                            }
                          },
                          "tech_qg_124": {
                            "label": "evaporation",
                            "children": {
                              "tech_impacts_evaporation": {
                                "label": "evaporation",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          }
                        }
                      },
                      "tech__8__1__ecological_soil": {
                        "label": "Soil",
                        "children": {
                          "tech_qg_125": {
                            "label": "soil moisture",
                            "children": {
                              "tech_impacts_soilmoisture": {
                                "label": "soil moisture",
                                "value": [
                                  {
                                    "layout": "stacked",
                                    "template": "raw",
                                    "additional_translations": {
                                      "label_left": "decreased",
                                      "label_right": "increased"
                                    },
                                    "key": "soil moisture",
                                    "value": "2",
                                    "level": 4,
                                    "all_values": [
                                      [
                                        1,
                                        "-3"
                                      ],
                                      [
                                        1,
                                        "-2"
                                      ],
                                      [
                                        1,
                                        "-1"
                                      ],
                                      [
                                        1,
                                        "0"
                                      ],
                                      [
                                        1,
                                        "1"
                                      ],
                                      [
                                        5,
                                        "2"
                                      ],
                                      [
                                        1,
                                        "3"
                                      ]
                                    ],
                                    "label_text_direction": None
                                  }
                                ]
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Quantity before SLM",
                                    "value": None
                                  }
                                ]
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Quantity after SLM",
                                    "value": None
                                  }
                                ]
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Comments/ specify",
                                    "value": None
                                  }
                                ]
                              }
                            }
                          },
                          "tech_qg_126": {
                            "label": "soil cover",
                            "children": {
                              "tech_impacts_soilcover": {
                                "label": "soil cover",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_127": {
                            "label": "soil loss",
                            "children": {
                              "tech_impacts_soilloss": {
                                "label": "soil loss",
                                "value": [
                                  {
                                    "layout": "stacked",
                                    "template": "raw",
                                    "additional_translations": {
                                      "label_left": "increased",
                                      "label_right": "decreased"
                                    },
                                    "key": "soil loss",
                                    "value": "2",
                                    "level": 4,
                                    "all_values": [
                                      [
                                        1,
                                        "-3"
                                      ],
                                      [
                                        1,
                                        "-2"
                                      ],
                                      [
                                        1,
                                        "-1"
                                      ],
                                      [
                                        1,
                                        "0"
                                      ],
                                      [
                                        1,
                                        "1"
                                      ],
                                      [
                                        5,
                                        "2"
                                      ],
                                      [
                                        1,
                                        "3"
                                      ]
                                    ],
                                    "label_text_direction": None
                                  }
                                ]
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Quantity before SLM",
                                    "value": None
                                  }
                                ]
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Quantity after SLM",
                                    "value": None
                                  }
                                ]
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Comments/ specify",
                                    "value": None
                                  }
                                ]
                              }
                            }
                          },
                          "tech_qg_128": {
                            "label": "soil accumulation",
                            "children": {
                              "tech_impacts_soilaccumulation": {
                                "label": "soil accumulation",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_129": {
                            "label": "soil crusting/ sealing",
                            "children": {
                              "tech_impacts_soilcrusting": {
                                "label": "soil crusting/ sealing",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_130": {
                            "label": "soil compaction",
                            "children": {
                              "tech_impacts_soilcompaction": {
                                "label": "soil compaction",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_131": {
                            "label": "nutrient cycling/ recharge",
                            "children": {
                              "tech_impacts_nutrientcycling": {
                                "label": "nutrient cycling/ recharge",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_132": {
                            "label": "salinity",
                            "children": {
                              "tech_impacts_soilsalinity": {
                                "label": "salinity",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_133": {
                            "label": "soil organic matter/ below ground C",
                            "children": {
                              "tech_impacts_soilorganicmatter": {
                                "label": "soil organic matter/ below ground C",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_134": {
                            "label": "acidity",
                            "children": {
                              "tech_impacts_soilacidity": {
                                "label": "acidity",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          }
                        }
                      },
                      "tech__8__1__ecological_biodiversity": {
                        "label": "Biodiversity: vegetation, animals",
                        "children": {
                          "tech_qg_167": {
                            "label": "Vegetation cover",
                            "children": {
                              "tech_impacts_vegcover": {
                                "label": "vegetation cover",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_140": {
                            "label": "biomass/ above ground C",
                            "children": {
                              "tech_impacts_biomass": {
                                "label": "biomass/ above ground C",
                                "value": [
                                  {
                                    "layout": "stacked",
                                    "template": "raw",
                                    "additional_translations": {
                                      "label_left": "decreased",
                                      "label_right": "increased"
                                    },
                                    "key": "biomass/ above ground C",
                                    "value": "2",
                                    "level": 4,
                                    "all_values": [
                                      [
                                        1,
                                        "-3"
                                      ],
                                      [
                                        1,
                                        "-2"
                                      ],
                                      [
                                        1,
                                        "-1"
                                      ],
                                      [
                                        1,
                                        "0"
                                      ],
                                      [
                                        1,
                                        "1"
                                      ],
                                      [
                                        5,
                                        "2"
                                      ],
                                      [
                                        1,
                                        "3"
                                      ]
                                    ],
                                    "label_text_direction": None
                                  }
                                ]
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Quantity before SLM",
                                    "value": None
                                  }
                                ]
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Quantity after SLM",
                                    "value": None
                                  }
                                ]
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Comments/ specify",
                                    "value": "Due to more moisture"
                                  }
                                ]
                              }
                            }
                          },
                          "tech_qg_136": {
                            "label": "plant diversity",
                            "children": {
                              "tech_impacts_plantdiversity": {
                                "label": "plant diversity",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_137": {
                            "label": "invasive alien species",
                            "children": {
                              "tech_impacts_invasivespecies": {
                                "label": "invasive alien species",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_135": {
                            "label": "animal diversity",
                            "children": {
                              "tech_impacts_animaldiversity": {
                                "label": "animal diversity",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_138": {
                            "label": "beneficial species",
                            "children": {
                              "tech_impacts_beneficialspecies": {
                                "label": "beneficial species (predators, earthworms, pollinators)",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_139": {
                            "label": "habitat diversity",
                            "children": {
                              "tech_impacts_habitatdiversity": {
                                "label": "habitat diversity",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_145": {
                            "label": "pest/ disease control",
                            "children": {
                              "tech_impacts_pestcontrol": {
                                "label": "pest/ disease control",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          }
                        }
                      },
                      "tech__8__1__ecological_climate": {
                        "label": "Climate and disaster risk reduction",
                        "children": {
                          "tech_qg_142": {
                            "label": "flood impacts",
                            "children": {
                              "tech_impacts_floodimpacts": {
                                "label": "flood impacts",
                                "value": [
                                  {
                                    "layout": "stacked",
                                    "template": "raw",
                                    "additional_translations": {
                                      "label_left": "increased",
                                      "label_right": "decreased"
                                    },
                                    "key": "flood impacts",
                                    "value": "-2",
                                    "level": 1,
                                    "all_values": [
                                      [
                                        1,
                                        "-3"
                                      ],
                                      [
                                        5,
                                        "-2"
                                      ],
                                      [
                                        1,
                                        "-1"
                                      ],
                                      [
                                        1,
                                        "0"
                                      ],
                                      [
                                        1,
                                        "1"
                                      ],
                                      [
                                        1,
                                        "2"
                                      ],
                                      [
                                        1,
                                        "3"
                                      ]
                                    ],
                                    "label_text_direction": None
                                  }
                                ]
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Quantity before SLM",
                                    "value": None
                                  }
                                ]
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Quantity after SLM",
                                    "value": None
                                  }
                                ]
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Comments/ specify",
                                    "value": None
                                  }
                                ]
                              }
                            }
                          },
                          "tech_qg_228": {
                            "label": "landslides/ debris flows",
                            "children": {
                              "tech_impacts_landslides": {
                                "label": "landslides/ debris flows",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_220": {
                            "label": "drought impacts",
                            "children": {
                              "tech_impacts_droughtimpacts": {
                                "label": "drought impacts",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_221": {
                            "label": "impacts of cyclones, rain storms",
                            "children": {
                              "tech_impacts_cyclones": {
                                "label": "impacts of cyclones, rain storms",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_141": {
                            "label": "emission of carbon and greenhouse gases",
                            "children": {
                              "tech_impacts_emissioncarbon": {
                                "label": "emission of carbon and greenhouse gases",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_143": {
                            "label": "fire risk",
                            "children": {
                              "tech_impacts_firerisk": {
                                "label": "fire risk",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_144": {
                            "label": "wind velocity",
                            "children": {
                              "tech_impacts_windvelocity": {
                                "label": "wind velocity",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_188": {
                            "label": "micro-climate",
                            "children": {
                              "tech_impacts_microclimate": {
                                "label": "micro-climate",
                                "value": ""
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": ""
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": ""
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": ""
                              }
                            }
                          }
                        }
                      },
                      "tech__8__1__ecological_other": {
                        "label": "Other ecological impacts",
                        "children": {
                          "tech_qg_189": {
                            "label": "other",
                            "children": {
                              "tech_impacts_other_specify": {
                                "label": "Specify",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Specify",
                                    "value": "disturbance of soil and vegetation during excavation works"
                                  }
                                ]
                              },
                              "tech_impacts_other_labelleft": {
                                "label": "[Label left]",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "[Label left]",
                                    "value": "increased"
                                  }
                                ]
                              },
                              "tech_impacts_other_measure": {
                                "label": "[Measure]",
                                "value": [
                                  {
                                    "layout": "stacked",
                                    "template": "raw",
                                    "additional_translations": {
                                      "label_left": None,
                                      "label_right": None
                                    },
                                    "key": "[Measure]",
                                    "value": "-1",
                                    "level": 1,
                                    "all_values": [
                                      [
                                        1,
                                        "-3"
                                      ],
                                      [
                                        1,
                                        "-2"
                                      ],
                                      [
                                        5,
                                        "-1"
                                      ],
                                      [
                                        1,
                                        "0"
                                      ],
                                      [
                                        1,
                                        "1"
                                      ],
                                      [
                                        1,
                                        "2"
                                      ],
                                      [
                                        1,
                                        "3"
                                      ]
                                    ],
                                    "label_text_direction": None
                                  }
                                ]
                              },
                              "tech_impacts_other_labelright": {
                                "label": "[Label right]",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "[Label right]",
                                    "value": "decreased"
                                  }
                                ]
                              },
                              "tech_impacts_quant_before": {
                                "label": "Quantity before SLM",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Quantity before SLM",
                                    "value": None
                                  }
                                ]
                              },
                              "tech_impacts_quant_after": {
                                "label": "Quantity after SLM",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Quantity after SLM",
                                    "value": None
                                  }
                                ]
                              },
                              "tech_impacts_specify": {
                                "label": "Comments/ specify",
                                "value": [
                                  {
                                    "template": "raw",
                                    "additional_translations": {},
                                    "key": "Comments/ specify",
                                    "value": None
                                  }
                                ]
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              },
              "tech__6__2": {
                "label": "Off-site impacts the Technology has shown",
                "children": {
                  "tech_qg_146": {
                    "label": "water availability",
                    "children": {
                      "tech_impacts_wateravailability": {
                        "label": "water availability (groundwater, springs)",
                        "value": [
                          {
                            "layout": "stacked",
                            "template": "raw",
                            "additional_translations": {
                              "label_left": "decreased",
                              "label_right": "increased"
                            },
                            "key": "water availability (groundwater, springs)",
                            "value": "1",
                            "level": 3,
                            "all_values": [
                              [
                                1,
                                "-3"
                              ],
                              [
                                1,
                                "-2"
                              ],
                              [
                                1,
                                "-1"
                              ],
                              [
                                1,
                                "0"
                              ],
                              [
                                5,
                                "1"
                              ],
                              [
                                1,
                                "2"
                              ],
                              [
                                1,
                                "3"
                              ]
                            ],
                            "label_text_direction": None
                          }
                        ]
                      },
                      "tech_impacts_quant_before": {
                        "label": "Quantity before SLM",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Quantity before SLM",
                            "value": None
                          }
                        ]
                      },
                      "tech_impacts_quant_after": {
                        "label": "Quantity after SLM",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Quantity after SLM",
                            "value": None
                          }
                        ]
                      },
                      "tech_impacts_specify": {
                        "label": "Comments/ specify",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Comments/ specify",
                            "value": None
                          }
                        ]
                      }
                    }
                  },
                  "tech_qg_148": {
                    "label": "reliable and stable stream flows in dry season",
                    "children": {
                      "tech_impacts_reliableflows": {
                        "label": "reliable and stable stream flows in dry season (incl. low flows)",
                        "value": ""
                      },
                      "tech_impacts_quant_before": {
                        "label": "Quantity before SLM",
                        "value": ""
                      },
                      "tech_impacts_quant_after": {
                        "label": "Quantity after SLM",
                        "value": ""
                      },
                      "tech_impacts_specify": {
                        "label": "Comments/ specify",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_147": {
                    "label": "downstream flooding",
                    "children": {
                      "tech_impacts_downstreamflooding": {
                        "label": "downstream flooding (undesired)",
                        "value": [
                          {
                            "layout": "stacked",
                            "template": "raw",
                            "additional_translations": {
                              "label_left": "increased",
                              "label_right": "reduced"
                            },
                            "key": "downstream flooding (undesired)",
                            "value": "2",
                            "level": 4,
                            "all_values": [
                              [
                                1,
                                "-3"
                              ],
                              [
                                1,
                                "-2"
                              ],
                              [
                                1,
                                "-1"
                              ],
                              [
                                1,
                                "0"
                              ],
                              [
                                1,
                                "1"
                              ],
                              [
                                5,
                                "2"
                              ],
                              [
                                1,
                                "3"
                              ]
                            ],
                            "label_text_direction": None
                          }
                        ]
                      },
                      "tech_impacts_quant_before": {
                        "label": "Quantity before SLM",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Quantity before SLM",
                            "value": None
                          }
                        ]
                      },
                      "tech_impacts_quant_after": {
                        "label": "Quantity after SLM",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Quantity after SLM",
                            "value": None
                          }
                        ]
                      },
                      "tech_impacts_specify": {
                        "label": "Comments/ specify",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Comments/ specify",
                            "value": None
                          }
                        ]
                      }
                    }
                  },
                  "tech_qg_149": {
                    "label": "downstream siltation",
                    "children": {
                      "tech_impacts_downstreamsiltation": {
                        "label": "downstream siltation",
                        "value": [
                          {
                            "layout": "stacked",
                            "template": "raw",
                            "additional_translations": {
                              "label_left": "increased",
                              "label_right": "decreased"
                            },
                            "key": "downstream siltation",
                            "value": "2",
                            "level": 4,
                            "all_values": [
                              [
                                1,
                                "-3"
                              ],
                              [
                                1,
                                "-2"
                              ],
                              [
                                1,
                                "-1"
                              ],
                              [
                                1,
                                "0"
                              ],
                              [
                                1,
                                "1"
                              ],
                              [
                                5,
                                "2"
                              ],
                              [
                                1,
                                "3"
                              ]
                            ],
                            "label_text_direction": None
                          }
                        ]
                      },
                      "tech_impacts_quant_before": {
                        "label": "Quantity before SLM",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Quantity before SLM",
                            "value": None
                          }
                        ]
                      },
                      "tech_impacts_quant_after": {
                        "label": "Quantity after SLM",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Quantity after SLM",
                            "value": None
                          }
                        ]
                      },
                      "tech_impacts_specify": {
                        "label": "Comments/ specify",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Comments/ specify",
                            "value": "And sedimentation"
                          }
                        ]
                      }
                    }
                  },
                  "tech_qg_150": {
                    "label": "groundwater/ river pollution",
                    "children": {
                      "tech_impacts_groundwaterpollution": {
                        "label": "groundwater/ river pollution",
                        "value": ""
                      },
                      "tech_impacts_quant_before": {
                        "label": "Quantity before SLM",
                        "value": ""
                      },
                      "tech_impacts_quant_after": {
                        "label": "Quantity after SLM",
                        "value": ""
                      },
                      "tech_impacts_specify": {
                        "label": "Comments/ specify",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_151": {
                    "label": "buffering/ filtering capacity",
                    "children": {
                      "tech_impacts_bufferingcapacity": {
                        "label": "buffering/ filtering capacity (by soil, vegetation, wetlands)",
                        "value": ""
                      },
                      "tech_impacts_quant_before": {
                        "label": "Quantity before SLM",
                        "value": ""
                      },
                      "tech_impacts_quant_after": {
                        "label": "Quantity after SLM",
                        "value": ""
                      },
                      "tech_impacts_specify": {
                        "label": "Comments/ specify",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_152": {
                    "label": "wind transported sediments",
                    "children": {
                      "tech_impacts_windtransportedsediments": {
                        "label": "wind transported sediments",
                        "value": ""
                      },
                      "tech_impacts_quant_before": {
                        "label": "Quantity before SLM",
                        "value": ""
                      },
                      "tech_impacts_quant_after": {
                        "label": "Quantity after SLM",
                        "value": ""
                      },
                      "tech_impacts_specify": {
                        "label": "Comments/ specify",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_153": {
                    "label": "damage on neighbours' fields",
                    "children": {
                      "tech_impacts_damageneighbourfield": {
                        "label": "damage on neighbours' fields",
                        "value": ""
                      },
                      "tech_impacts_quant_before": {
                        "label": "Quantity before SLM",
                        "value": ""
                      },
                      "tech_impacts_quant_after": {
                        "label": "Quantity after SLM",
                        "value": ""
                      },
                      "tech_impacts_specify": {
                        "label": "Comments/ specify",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_154": {
                    "label": "damage on public/ private infrastructure",
                    "children": {
                      "tech_impacts_damageinfrastructure": {
                        "label": "damage on public/ private infrastructure",
                        "value": ""
                      },
                      "tech_impacts_quant_before": {
                        "label": "Quantity before SLM",
                        "value": ""
                      },
                      "tech_impacts_quant_after": {
                        "label": "Quantity after SLM",
                        "value": ""
                      },
                      "tech_impacts_specify": {
                        "label": "Comments/ specify",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_155": {
                    "label": "impact of greenhouse gases",
                    "children": {
                      "tech_impacts_impactgreenhousegases": {
                        "label": "impact of greenhouse gases",
                        "value": ""
                      },
                      "tech_impacts_quant_before": {
                        "label": "Quantity before SLM",
                        "value": ""
                      },
                      "tech_impacts_quant_after": {
                        "label": "Quantity after SLM",
                        "value": ""
                      },
                      "tech_impacts_specify": {
                        "label": "Comments/ specify",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_190": {
                    "label": "other",
                    "children": {
                      "tech_impacts_other_specify": {
                        "label": "Specify",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Specify",
                            "value": "damage on agriculture fields"
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Specify",
                            "value": "As the site is closed, grazing pressure shifts elsewhere"
                          }
                        ]
                      },
                      "tech_impacts_other_labelleft": {
                        "label": "[Label left]",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "[Label left]",
                            "value": "improved"
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "[Label left]",
                            "value": None
                          }
                        ]
                      },
                      "tech_impacts_other_measure": {
                        "label": "[Measure]",
                        "value": [
                          {
                            "layout": "stacked",
                            "template": "raw",
                            "additional_translations": {
                              "label_left": None,
                              "label_right": None
                            },
                            "key": "[Measure]",
                            "value": "2",
                            "level": 4,
                            "all_values": [
                              [
                                1,
                                "-3"
                              ],
                              [
                                1,
                                "-2"
                              ],
                              [
                                1,
                                "-1"
                              ],
                              [
                                1,
                                "0"
                              ],
                              [
                                1,
                                "1"
                              ],
                              [
                                5,
                                "2"
                              ],
                              [
                                1,
                                "3"
                              ]
                            ],
                            "label_text_direction": None
                          },
                          {
                            "layout": "stacked",
                            "template": "raw",
                            "additional_translations": {
                              "label_left": None,
                              "label_right": None
                            },
                            "key": "[Measure]",
                            "value": "-1",
                            "level": 1,
                            "all_values": [
                              [
                                1,
                                "-3"
                              ],
                              [
                                1,
                                "-2"
                              ],
                              [
                                5,
                                "-1"
                              ],
                              [
                                1,
                                "0"
                              ],
                              [
                                1,
                                "1"
                              ],
                              [
                                1,
                                "2"
                              ],
                              [
                                1,
                                "3"
                              ]
                            ],
                            "label_text_direction": None
                          }
                        ]
                      },
                      "tech_impacts_other_labelright": {
                        "label": "[Label right]",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "[Label right]",
                            "value": "reduced"
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "[Label right]",
                            "value": None
                          }
                        ]
                      },
                      "tech_impacts_quant_before": {
                        "label": "Quantity before SLM",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Quantity before SLM",
                            "value": None
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Quantity before SLM",
                            "value": None
                          }
                        ]
                      },
                      "tech_impacts_quant_after": {
                        "label": "Quantity after SLM",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Quantity after SLM",
                            "value": None
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Quantity after SLM",
                            "value": None
                          }
                        ]
                      },
                      "tech_impacts_specify": {
                        "label": "Comments/ specify",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Comments/ specify",
                            "value": None
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Comments/ specify",
                            "value": None
                          }
                        ]
                      }
                    }
                  },
                  "tech_qg_229": {
                    "label": "",
                    "children": {
                      "tech_impacts_comments": {
                        "label": "Comments regarding impact assessment",
                        "value": ""
                      }
                    }
                  }
                }
              },
              "tech__6__3": {
                "label": "Exposure and sensitivity of the Technology to gradual climate change and climate-related extremes/ disasters (as perceived by land users)",
                "children": {
                  "tech__8__3__gradual": {
                    "label": "Gradual climate change",
                    "children": {
                      "tech__8__3__gradual": {
                        "label": "Gradual climate change",
                        "children": {
                          "tech_qg_168": {
                            "label": "annual temperature",
                            "children": {
                              "tech_exposure_incrdecr": {
                                "label": "Type of climatic change/ extreme",
                                "value": [
                                  {
                                    "additional_translations": {},
                                    "key": "Type of climatic change/ extreme",
                                    "value": "increase",
                                    "template": "raw"
                                  }
                                ]
                              },
                              "tech_exposure_sensitivity": {
                                "label": "How does the Technology cope with it?",
                                "value": [
                                  {
                                    "additional_translations": {},
                                    "key": "How does the Technology cope with it?",
                                    "value": "well",
                                    "template": "raw"
                                  }
                                ]
                              }
                            }
                          },
                          "tech_qg_169": {
                            "label": "seasonal temperature",
                            "children": {
                              "tech_exposure_season": {
                                "label": "Season",
                                "value": ""
                              },
                              "tech_exposure_incrdecr": {
                                "label": "Type of climatic change/ extreme",
                                "value": ""
                              },
                              "tech_exposure_sensitivity": {
                                "label": "How does the Technology cope with it?",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_170": {
                            "label": "annual rainfall",
                            "children": {
                              "tech_exposure_incrdecr": {
                                "label": "Type of climatic change/ extreme",
                                "value": ""
                              },
                              "tech_exposure_sensitivity": {
                                "label": "How does the Technology cope with it?",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_171": {
                            "label": "seasonal rainfall",
                            "children": {
                              "tech_exposure_season": {
                                "label": "Season",
                                "value": ""
                              },
                              "tech_exposure_incrdecr": {
                                "label": "Type of climatic change/ extreme",
                                "value": ""
                              },
                              "tech_exposure_sensitivity": {
                                "label": "How does the Technology cope with it?",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_172": {
                            "label": "other gradual climate change",
                            "children": {
                              "tech_exposure_other_specify": {
                                "label": "other (specify)",
                                "value": ""
                              },
                              "tech_exposure_incrdecr": {
                                "label": "Type of climatic change/ extreme",
                                "value": ""
                              },
                              "tech_exposure_sensitivity": {
                                "label": "How does the Technology cope with it?",
                                "value": ""
                              }
                            }
                          }
                        }
                      }
                    }
                  },
                  "tech__8__3__climaterelated": {
                    "label": "Climate-related extremes (disasters)",
                    "children": {
                      "tech__8__3__meteorological": {
                        "label": "Meteorological disasters",
                        "children": {
                          "tech_qg_177": {
                            "label": "tropical storm",
                            "children": {
                              "tech_exposure_sensitivity": {
                                "label": "How does the Technology cope with it?",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_178": {
                            "label": "extra-tropical cyclone",
                            "children": {
                              "tech_exposure_sensitivity": {
                                "label": "How does the Technology cope with it?",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_179": {
                            "label": "local rainstorm",
                            "children": {
                              "tech_exposure_sensitivity": {
                                "label": "How does the Technology cope with it?",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_193": {
                            "label": "local thunderstorm",
                            "children": {
                              "tech_exposure_sensitivity": {
                                "label": "How does the Technology cope with it?",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_194": {
                            "label": "local hailstorm",
                            "children": {
                              "tech_exposure_sensitivity": {
                                "label": "How does the Technology cope with it?",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_195": {
                            "label": "local snowstorm",
                            "children": {
                              "tech_exposure_sensitivity": {
                                "label": "How does the Technology cope with it?",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_196": {
                            "label": "local sandstorm/ duststorm",
                            "children": {
                              "tech_exposure_sensitivity": {
                                "label": "How does the Technology cope with it?",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_197": {
                            "label": "local windstorm",
                            "children": {
                              "tech_exposure_sensitivity": {
                                "label": "How does the Technology cope with it?",
                                "value": [
                                  {
                                    "additional_translations": {},
                                    "key": "How does the Technology cope with it?",
                                    "value": "well",
                                    "template": "raw"
                                  }
                                ]
                              }
                            }
                          },
                          "tech_qg_198": {
                            "label": "tornado",
                            "children": {
                              "tech_exposure_sensitivity": {
                                "label": "How does the Technology cope with it?",
                                "value": ""
                              }
                            }
                          }
                        }
                      },
                      "tech__8__3__climatological": {
                        "label": "Climatological disasters",
                        "children": {
                          "tech_qg_199": {
                            "label": "heatwave",
                            "children": {
                              "tech_exposure_sensitivity": {
                                "label": "How does the Technology cope with it?",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_200": {
                            "label": "cold wave",
                            "children": {
                              "tech_exposure_sensitivity": {
                                "label": "How does the Technology cope with it?",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_201": {
                            "label": "extreme winter conditions",
                            "children": {
                              "tech_exposure_sensitivity": {
                                "label": "How does the Technology cope with it?",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_202": {
                            "label": "drought",
                            "children": {
                              "tech_exposure_sensitivity": {
                                "label": "How does the Technology cope with it?",
                                "value": [
                                  {
                                    "additional_translations": {},
                                    "key": "How does the Technology cope with it?",
                                    "value": "well",
                                    "template": "raw"
                                  }
                                ]
                              }
                            }
                          },
                          "tech_qg_203": {
                            "label": "forest fire",
                            "children": {
                              "tech_exposure_sensitivity": {
                                "label": "How does the Technology cope with it?",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_204": {
                            "label": "land fire",
                            "children": {
                              "tech_exposure_sensitivity": {
                                "label": "How does the Technology cope with it?",
                                "value": ""
                              }
                            }
                          }
                        }
                      },
                      "tech__8__3__hydrological": {
                        "label": "Hydrological disasters",
                        "children": {
                          "tech_qg_205": {
                            "label": "general (river) flood",
                            "children": {
                              "tech_exposure_sensitivity": {
                                "label": "How does the Technology cope with it?",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_206": {
                            "label": "flash flood",
                            "children": {
                              "tech_exposure_sensitivity": {
                                "label": "How does the Technology cope with it?",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_207": {
                            "label": "storm surge/ coastal flood",
                            "children": {
                              "tech_exposure_sensitivity": {
                                "label": "How does the Technology cope with it?",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_208": {
                            "label": "landslide",
                            "children": {
                              "tech_exposure_sensitivity": {
                                "label": "How does the Technology cope with it?",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_209": {
                            "label": "avalanche",
                            "children": {
                              "tech_exposure_sensitivity": {
                                "label": "How does the Technology cope with it?",
                                "value": ""
                              }
                            }
                          }
                        }
                      },
                      "tech__8__3__biological": {
                        "label": "Biological disasters",
                        "children": {
                          "tech_qg_210": {
                            "label": "epidemic diseases",
                            "children": {
                              "tech_exposure_sensitivity": {
                                "label": "How does the Technology cope with it?",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_211": {
                            "label": "insect/ worm infestation",
                            "children": {
                              "tech_exposure_sensitivity": {
                                "label": "How does the Technology cope with it?",
                                "value": ""
                              }
                            }
                          }
                        }
                      },
                      "tech__8__3__otherclimate": {
                        "label": "Other climate-related extremes (disasters)",
                        "children": {
                          "tech_qg_212": {
                            "label": "other",
                            "children": {
                              "tech_exposure_other_specify": {
                                "label": "other (specify)",
                                "value": ""
                              },
                              "tech_exposure_sensitivity": {
                                "label": "How does the Technology cope with it?",
                                "value": ""
                              }
                            }
                          }
                        }
                      }
                    }
                  },
                  "tech__8__3__other": {
                    "label": "Other climate-related consequences",
                    "children": {
                      "tech__8__3__other": {
                        "label": "Other climate-related consequences",
                        "children": {
                          "tech_qg_213": {
                            "label": "extended growing period",
                            "children": {
                              "tech_exposure_sensitivity": {
                                "label": "How does the Technology cope with it?",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_214": {
                            "label": "reduced growing period",
                            "children": {
                              "tech_exposure_sensitivity": {
                                "label": "How does the Technology cope with it?",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_215": {
                            "label": "sea level rise",
                            "children": {
                              "tech_exposure_sensitivity": {
                                "label": "How does the Technology cope with it?",
                                "value": ""
                              }
                            }
                          },
                          "tech_qg_216": {
                            "label": "other",
                            "children": {
                              "tech_exposure_other_specify": {
                                "label": "other (specify)",
                                "value": [
                                  {
                                    "additional_translations": {},
                                    "key": "other (specify)",
                                    "value": "Extreme precipitation events especially if the technology is applied on steep slopes.",
                                    "template": "raw"
                                  }
                                ]
                              },
                              "tech_exposure_sensitivity": {
                                "label": "How does the Technology cope with it?",
                                "value": [
                                  {
                                    "additional_translations": {},
                                    "key": "How does the Technology cope with it?",
                                    "value": "not well",
                                    "template": "raw"
                                  }
                                ]
                              }
                            }
                          }
                        }
                      }
                    }
                  },
                  "tech__8__3__comments": {
                    "label": "Comments",
                    "children": {
                      "tech_qg_180": {
                        "label": "",
                        "children": {
                          "tech_tolerance_comments": {
                            "label": "Comments",
                            "value": [
                              {
                                "additional_translations": {},
                                "key": "Comments",
                                "value": "Increase size, stable bunds stabilized with vegetation",
                                "template": "raw"
                              }
                            ]
                          }
                        }
                      }
                    }
                  }
                }
              },
              "tech__6__4": {
                "label": "Cost-benefit analysis",
                "children": {
                  "tech_qg_181": {
                    "label": "How do the benefits compare with the establishment costs (from land usersâ€™ perspective)?",
                    "children": {
                      "tech_costbenefit_est_short": {
                        "label": "Short-term returns",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Short-term returns",
                            "values": [
                              "slightly negative"
                            ]
                          }
                        ]
                      },
                      "tech_costbenefit_est_long": {
                        "label": "Long-term returns",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Long-term returns",
                            "values": [
                              "positive"
                            ]
                          }
                        ]
                      }
                    }
                  },
                  "tech_qg_182": {
                    "label": "How do the benefits compare with the maintenance/ recurrent costs (from land users' perspective)?",
                    "children": {
                      "tech_costbenefit_est_short": {
                        "label": "Short-term returns",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Short-term returns",
                            "values": [
                              "neutral/ balanced"
                            ]
                          }
                        ]
                      },
                      "tech_costbenefit_est_long": {
                        "label": "Long-term returns",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Long-term returns",
                            "values": [
                              "very positive"
                            ]
                          }
                        ]
                      }
                    }
                  },
                  "tech_qg_183": {
                    "label": "",
                    "children": {
                      "tech_costbenefit_comments": {
                        "label": "Comments",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Comments",
                            "value": "The benefits will be more in the long term when trees, shrubs and fodder grasses are ready to harvest.",
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  }
                }
              },
              "tech__6__5": {
                "label": "Adoption of the Technology",
                "children": {
                  "tech_qg_191": {
                    "label": "",
                    "children": {
                      "tech_adoption_percentage": {
                        "label": "How many land users in the area have adopted/implemented the Technology?",
                        "value": [
                          {
                            "label_position": "none",
                            "additional_translations": {},
                            "key": "How many land users in the area have adopted/implemented the Technology?",
                            "values": [],
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_adoption_quantify": {
                        "label": "If available, quantify (no. of households and/ or area covered)",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "If available, quantify (no. of households and/ or area covered)",
                            "value": None,
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_adoption_spontaneously": {
                        "label": "Of all those who have adopted the Technology, how many have did so spontaneously, i.e. without receiving any material incentives/ payments?",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Of all those who have adopted the Technology, how many have did so spontaneously, i.e. without receiving any material incentives/ payments?",
                            "values": [],
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_adoption_comments": {
                        "label": "Comments",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Comments",
                            "value": "Comments on acceptance with external material support: Appropriate information is not available.\r\n\r\nComments on spontaneous adoption: Only soil bunds have been applied by a few farmers on their private lands.",
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  }
                }
              },
              "tech__6__6": {
                "label": "Adaptation",
                "children": {
                  "tech_qg_230": {
                    "label": "",
                    "children": {
                      "tech_adaptation_yes": {
                        "label": "Has the Technology been modified recently to adapt to changing conditions?",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_192": {
                    "label": "",
                    "children": {
                      "tech_adaptation_modification": {
                        "label": "If yes, indicate to which changing conditions it was adapted",
                        "value": ""
                      },
                      "tech_adaptation_modification_other": {
                        "label": "other (specify)",
                        "value": ""
                      },
                      "tech_adaptation_specify": {
                        "label": "Specify adaptation of the Technology (design, material/ species, etc.)",
                        "value": ""
                      }
                    }
                  }
                }
              },
              "tech__6__7": {
                "label": "Strengths/ advantages/ opportunities of the Technology",
                "children": {
                  "qg_strengths_landusers": {
                    "label": "",
                    "children": {
                      "strengths_landuser": {
                        "label": "Strengths/ advantages/ opportunities in the land userâ€™s view",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Strengths/ advantages/ opportunities in the land userâ€™s view",
                            "value": "The technology helps to create SLM based job opportunities for many people.\r\n\r\nHow can they be sustained / enhanced? Needs external support/projects."
                          }
                        ]
                      }
                    }
                  },
                  "qg_strengths_compiler": {
                    "label": "",
                    "children": {
                      "strengths_compiler": {
                        "label": "Strengths/ advantages/ opportunities in the compilerâ€™s or other key resource personâ€™s view",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Strengths/ advantages/ opportunities in the compilerâ€™s or other key resource personâ€™s view",
                            "value": "Demonstration of link between SLM measures and water source.\r\n\r\nHow can they be sustained / enhanced? Conducting training and showing drawing."
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Strengths/ advantages/ opportunities in the compilerâ€™s or other key resource personâ€™s view",
                            "value": "Technical knowledge of community enhanced.\r\n\r\nHow can they be sustained / enhanced? Share more aspects of the technology, where to apply and how."
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Strengths/ advantages/ opportunities in the compilerâ€™s or other key resource personâ€™s view",
                            "value": "Flood reduction, greening of the area, increase the spring water.\r\n\r\nHow can they be sustained / enhanced? Cultivate native plants, share experiences with more communities and SLM specialists."
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Strengths/ advantages/ opportunities in the compilerâ€™s or other key resource personâ€™s view",
                            "value": "Good for land rehabilitation (extremely degraded lands).\r\n\r\nHow can they be sustained / enhanced? Always combine with vegetative and management measures."
                          }
                        ]
                      }
                    }
                  }
                }
              },
              "tech__6__8": {
                "label": "Weaknesses/ disadvantages/ risks of the Technology and ways of overcoming them",
                "children": {
                  "qg_weaknesses_landusers": {
                    "label": "",
                    "children": {
                      "weaknesses_landuser": {
                        "label": "Weaknesses/ disadvantages/ risks in the land userâ€™s view",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Weaknesses/ disadvantages/ risks in the land userâ€™s view",
                            "value": "Farmers do not prefer to construct this technology because it requires soil excavation/disturbance."
                          }
                        ]
                      },
                      "weaknesses_overcome": {
                        "label": "How can they be overcome?",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "How can they be overcome?",
                            "value": "One needs to show how such measures have been applied in other parts of the world for multiple benefits through action research."
                          }
                        ]
                      }
                    }
                  },
                  "qg_weaknesses_compiler": {
                    "label": "",
                    "children": {
                      "weaknesses_compiler": {
                        "label": "Weaknesses/ disadvantages/ risks in the compilerâ€™s or other key resource personâ€™s view",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Weaknesses/ disadvantages/ risks in the compilerâ€™s or other key resource personâ€™s view",
                            "value": "Site selection"
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Weaknesses/ disadvantages/ risks in the compilerâ€™s or other key resource personâ€™s view",
                            "value": "Higher cost of establishment of the technology."
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Weaknesses/ disadvantages/ risks in the compilerâ€™s or other key resource personâ€™s view",
                            "value": "Technical design"
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "Weaknesses/ disadvantages/ risks in the compilerâ€™s or other key resource personâ€™s view",
                            "value": "Few vegetative measures"
                          }
                        ]
                      },
                      "weaknesses_overcome": {
                        "label": "How can they be overcome?",
                        "value": [
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "How can they be overcome?",
                            "value": "Apply technology at suitable site that has proper slope and is really degraded. Avoid places where there is already good vegetation cover."
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "How can they be overcome?",
                            "value": "Encourage the community for more contribution or apply where absolutely necessary."
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "How can they be overcome?",
                            "value": "The designer should research more about the site and discuss with the skilled people of the community before designing."
                          },
                          {
                            "template": "raw",
                            "additional_translations": {},
                            "key": "How can they be overcome?",
                            "value": "plant fodder grasses and adapted trees between trenches."
                          }
                        ]
                      }
                    }
                  }
                }
              }
            }
          },
          "tech__7": {
            "label": "References and links",
            "children": {
              "tech__7__1": {
                "label": "Methods/ sources of information",
                "children": {
                  "qg_sources": {
                    "label": "",
                    "children": {
                      "sources_used": {
                        "label": "Which of the following methods/ sources of information were used?",
                        "value": ""
                      }
                    }
                  },
                  "qg_sources_field": {
                    "label": "",
                    "children": {
                      "sources_specify": {
                        "label": "Specify (e.g. number of informants)",
                        "value": ""
                      }
                    }
                  },
                  "qg_sources_interviews_landusers": {
                    "label": "",
                    "children": {
                      "sources_specify": {
                        "label": "Specify (e.g. number of informants)",
                        "value": ""
                      }
                    }
                  },
                  "qg_sources_interviews_experts": {
                    "label": "",
                    "children": {
                      "sources_specify": {
                        "label": "Specify (e.g. number of informants)",
                        "value": ""
                      }
                    }
                  },
                  "qg_sources_compilation": {
                    "label": "",
                    "children": {
                      "sources_specify": {
                        "label": "Specify (e.g. number of informants)",
                        "value": ""
                      }
                    }
                  },
                  "qg_sources_other": {
                    "label": "",
                    "children": {
                      "sources_other": {
                        "label": "other (specify)",
                        "value": ""
                      },
                      "sources_specify": {
                        "label": "Specify (e.g. number of informants)",
                        "value": ""
                      }
                    }
                  }
                }
              },
              "tech__7__2": {
                "label": "References to available publications",
                "children": {
                  "qg_references": {
                    "label": "",
                    "children": {
                      "references_title": {
                        "label": "Title, author, year, ISBN",
                        "value": ""
                      },
                      "references_source": {
                        "label": "Available from where? Costs?",
                        "value": ""
                      }
                    }
                  }
                }
              },
              "tech__7__3": {
                "label": "Links to relevant information which is available online",
                "children": {
                  "qg_links": {
                    "label": "",
                    "children": {
                      "links_title": {
                        "label": "Title/ description",
                        "value": ""
                      },
                      "links_url": {
                        "label": "URL",
                        "value": ""
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }


@pytest.fixture()
def api_details_2():
    # corresponds to results[0] of api_list_1
    return {
      "section_specifications": {
        "label": "Specifications",
        "children": {
          "tech__2": {
            "label": "Description of the SLM Technology",
            "children": {
              "tech__2__6": {
                "label": "Date of implementation",
                "children": {
                  "tech_qg_160": {
                    "label": "",
                    "children": {
                      "tech_implementation_year": {
                        "label": "Indicate year of implementation",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "Indicate year of implementation",
                            "value": 2011,
                            "template": "raw"
                          }
                        ]
                      },
                      "tech_implementation_decades": {
                        "label": "If precise year is not known, indicate approximate date",
                        "value": [
                          {
                            "additional_translations": {},
                            "key": "If precise year is not known, indicate approximate date",
                            "values": [
                              "less than 10 years ago (recently)"
                            ],
                            "template": "raw"
                          }
                        ]
                      }
                    }
                  }
                }
              },
            }
          },
          "tech__3": {
            "label": "Classification of the SLM Technology",
            "children": {
              "tech__3__1": {
                "label": "Main purpose(s) of the Technology",
                "children": {
                  "tech_qg_6": {
                    "label": "",
                    "children": {
                      "tech_main_purpose": {
                        "label": "Main purpose(s) of the Technology (land userâ€™s perspective)",
                        "value": [
                          {
                            "label_position": "none",
                            "additional_translations": {},
                            "key": "Main purpose(s) of the Technology (land userâ€™s perspective)",
                            "values": [
                              "protect a watershed/ downstream areas â€“ in combination with other Technologies",
                            ],
                            "template": "raw"
                          },
                          {
                            "label_position": "none",
                            "additional_translations": {},
                            "key": "Main purpose(s) of the Technology (land userâ€™s perspective)",
                            "values": [
                              "reduce risk of disasters"
                            ],
                            "template": "raw"
                          }
                        ]
                      },
                    }
                  }
                }
              },
            },
          },
          "tech__4": {
            "label": "Technical specifications, implementation activities, inputs, and costs",
            "children": {
              "tech__4__5": {
                "label": "Costs and inputs needed for establishment",
                "children": {
                  "tech_qg_42": {
                    "label": "",
                    "children": {
                      "tech_input_est_total_estimation": {
                        "label": "If possible, break down the costs of establishment according to the following table, specifying inputs and costs per input. If you are unable to break down the costs, give an estimation of the total costs of establishing the Technology",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_36": {
                    "label": "Labour",
                    "children": {
                      "tech_input_est_specify": {
                        "label": "Specify input",
                        "value": [
                          {
                            "value": None,
                          }
                        ]
                      },
                      "tech_input_est_unit": {
                        "label": "Unit",
                        "value": [
                          {
                            "value": None,
                          }
                        ]
                      },
                    }
                  },
                }
              },
            }
          },
        }
      }
    }


@pytest.fixture()
def api_details_3():
    # corresponds to results[0] of api_list_1
    return {
      "section_specifications": {
        "label": "Specifications",
        "children": {
          "tech__4": {
            "label": "Technical specifications, implementation activities, inputs, and costs",
            "children": {
              "tech__4__5": {
                "label": "Costs and inputs needed for establishment",
                "children": {
                  "tech_qg_42": {
                    "label": "",
                    "children": {
                      "tech_input_est_total_estimation": {
                        "label": "If possible, break down the costs of establishment according to the following table, specifying inputs and costs per input. If you are unable to break down the costs, give an estimation of the total costs of establishing the Technology",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_36": {
                    "label": "Labour",
                    "children": {
                      "tech_input_est_specify": {
                        "label": "Specify input",
                        "value": [
                          {
                            "value": "Mano de obra",
                          }
                        ]
                      },
                      "tech_input_est_unit": {
                        "label": "Unit",
                        "value": [
                          {
                            "value": None,
                          }
                        ]
                      },
                    }
                  },
                }
              },
            }
          },
        }
      }
    }


@pytest.fixture()
def api_details_4():
    # corresponds to results[0] of api_list_1
    return {
      "section_specifications": {
        "label": "Specifications",
        "children": {
          "tech__4": {
            "label": "Technical specifications, implementation activities, inputs, and costs",
            "children": {
              "tech__4__5": {
                "label": "Costs and inputs needed for establishment",
                "children": {
                  "tech_qg_42": {
                    "label": "",
                    "children": {
                      "tech_input_est_total_estimation": {
                        "label": "If possible, break down the costs of establishment according to the following table, specifying inputs and costs per input. If you are unable to break down the costs, give an estimation of the total costs of establishing the Technology",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_36": {
                    "label": "Labour",
                    "children": {
                      "tech_input_est_specify": {
                        "label": "Specify input",
                        "value": [
                          {
                            "value": "Construction",
                          },
                          {
                            "value": "Macrophyte installation"
                          }
                        ]
                      },
                      "tech_input_est_unit": {
                        "label": "Unit",
                        "value": [
                          {
                            "value": None,
                          },
                          {
                            "value": None
                          }
                        ]
                      },
                    }
                  },
                }
              },
            }
          },
        }
      }
    }


@pytest.fixture()
def api_details_5():
    # corresponds to results[0] of api_list_1
    return {
      "section_specifications": {
        "label": "Specifications",
        "children": {
          "tech__4": {
            "label": "Technical specifications, implementation activities, inputs, and costs",
            "children": {
              "tech__4__5": {
                "label": "Costs and inputs needed for establishment",
                "children": {
                  "tech_qg_42": {
                    "label": "",
                    "children": {
                      "tech_input_est_total_estimation": {
                        "label": "If possible, break down the costs of establishment according to the following table, specifying inputs and costs per input. If you are unable to break down the costs, give an estimation of the total costs of establishing the Technology",
                        "value": ""
                      }
                    }
                  },
                  "tech_qg_36": {
                    "label": "Labour",
                    "children": {
                      "tech_input_est_specify": {
                        "label": "Specify input",
                        "value": [
                          {
                            "value": "Construction",
                          }
                        ]
                      },
                      "tech_input_est_unit": {
                        "label": "Unit",
                        "value": [
                          {
                            "value": 12.91,
                          }
                        ]
                      },
                    }
                  },
                }
              },
            }
          },
        }
      }
    }
