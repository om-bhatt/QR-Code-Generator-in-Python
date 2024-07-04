from flet import *
def main(page: Page):
    BG = '#041955'
    FWG = 'white'
    FG = '#3450a1'
    PINK = '#eb06ff'


    categories_card = Row(
        scroll='auto'

    )
    categories = ['Business','Family','Friends']
    for category in categories:
        categories_card.controls.append(
            Container(
                bgcolor='white12',
                height=110,
                width=170,
                border_radius=20,
                padding=15,
            
            )
        )


    first_page_contents= Container(
        content=Column
        (
            controls=[
            
                Row(alignment='spaceBetween',
                    
                    
                    
                    controls=[
                        Container(content=Icon(
                            icons.MENU)),
                        Row(
                            controls=[
                                Icon(icons.SEARCH),
                                Icon(icons.NOTIFICATIONS_OUTLINED)
                            ],
                        ),
                    ],
                ),
                Container(height=10),
                
                Text(
                    value = 'hell world'
                ),
                Text(
                    value='CATEGORIOUS'
                ),
                Container(
                    padding=padding.only(top=10,bottom=20,),
                    content=categories_card
                ),
            ],   
        ),
    )                                       
                                                           
                


        
    
    

    page_1=Container()
    page_2=Row(
        controls=[
            Container(
                width=400,
                height=850,
                bgcolor=FG,
                padding=padding.only(
                    top=50,left=20,
                    right=20,bottom=5
                ),
                content=Column(
                    controls=[
                        first_page_contents
                    ]
                )
            )
        ]
    )

    container=Container(
        width=400,height=850,bgcolor=BG,border_radius=35,
        content=Stack(
            controls=[
                page_1,
                page_2
            ]
        )
    )
    page.add(container)


app(target=main)