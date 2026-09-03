from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Part1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    Treatment = models.IntegerField()

class Group(BaseGroup):
    pass

class Player(BasePlayer):


    consent = models.BooleanField(
        label="<b>I agree </b> to participate in this study.",
        blank=False,
        widget = widgets.CheckboxInput
    )


    prolific_id = models.StringField(
        label=""
        ,
        blank=False
    )

    # --- Page 1: Individual information ---
    #age = models.FloatField(label="", max=99)

    gender = models.IntegerField(
        label="",
        choices=[[1, "Man"], [2, "Woman"], [3, "Other/prefer not to say"]],
        widget=widgets.RadioSelectHorizontal
    )

    #ethnicity = models.IntegerField(
        #label="",
        #choices=[[1, "White"], [2, "African American/Black"], [3, "Hispanic/Latino"],
                 #[4, "Asian/Asian American"], [5, "Mixed race"], [6, "Other"]],
       # widget=widgets.RadioSelect
    #)

    education = models.IntegerField(
        label="",
        choices=[[1, "8th Grade or lower"], [2, "Some High School"], [3, "High School degree/GED"],
                 [4, "Some College"], [5, "2-year College Degree"], [6, "4-year College Degree"],
                 [7, "Master's Degree"], [8, "Doctoral Degree"], [9, "Professional Degree (JD or MD)"]],
        widget=widgets.RadioSelect
    )

    marital_status = models.IntegerField(
        label="",
        choices=[[1, "Single"], [2, "Married"], [3, "Legally separated or divorced"], [4, "Widowed"]],
        widget=widgets.RadioSelect
    )

    zip_code = models.StringField(label="")

    employment_status = models.IntegerField(
        label="",
        choices=[[1, "Full-time employee"], [2, "Part-time employee"], [3, "Self-employed or small business owner"],
                 [4, "Unemployed and looking for work"], [5, "Student"],
                 [6, "Not currently working and not looking for work"], [7, "Retiree"]],
        widget=widgets.RadioSelect
    )

    occupation_employed = models.IntegerField(
        label=" ",
        choices=[
            [1, "Management, professional, and technical"],
            [2, "Service"],
            [3, "Sales and administrative"],
            [4, "Manual and skilled trades"],
            [5, "Transportation and logistics"],
            [6, "Other occupations"]
        ],
        blank=True,
        widget=widgets.RadioSelect
    )

    occupation_employed_text = models.StringField(
        label="",
        blank=True,
    )

    job_flexibility_hours = models.IntegerField(
        label="",
        choices=[
            [1, "Never"],
            [2, "Rarely"],
            [3, "Sometimes"],
            [4, "Frequently"]
        ],
        blank=True,
        widget=widgets.RadioSelectHorizontal
    )

    job_flexibility_overtime = models.IntegerField(
        label="",
        choices=[[1, "Never"], [2, "Rarely"], [3, "Sometimes"], [4, "Frequently"]],
        blank=True,
        widget=widgets.RadioSelectHorizontal
    )

    occupation_unemployed = models.IntegerField(
        label=" ",
        choices=[
            [1, "Management, professional, and technical"],
            [2, "Service"],
            [3, "Sales and administrative"],
            [4, "Manual and skilled trades"],
            [5, "Transportation and logistics"],
            [6, "Other occupations"]
        ],
        blank=True,
        widget=widgets.RadioSelect
    )

    occupation_unemployed_text = models.StringField(
        label="",
        blank=True,
    )

    patience_scale = models.IntegerField(
        label="",
        choices=[[0, "0 (Completely unwilling) "],[1, "1"], [2, "2"], [3, "3"], [4, "4"], [5, "5"],
                 [6, "6 (Very willing)"]],
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )

    risk_scale = models.IntegerField(
        label="",
        choices=[[0, "0 (Completely unwilling)"], [1, "1"], [2, "2"], [3, "3"], [4, "4"], [5, "5"],
                 [6, "6 (Very willing)"]],
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )

    # --- Household info: Page 2 ---
    household_size = models.IntegerField(
        label=(
            ""
        ),
    choices=[[1, "1"], [2, "2"], [3, "3"], [4, "4"], [5, "5"],
                 [6, "6"], [7, "7"], [8, "8"], [9, "9"], [10, "10 or more"]],
        widget=widgets.RadioSelectHorizontal
    )

    household_children = models.IntegerField(
        label=(
            ""
        ),
        choices=[[0, "0"],[1, "1"], [2, "2"], [3, "3"], [4, "4"], [5, "5 or more"]],
        widget=widgets.RadioSelectHorizontal
    )

    residence_owner = models.IntegerField(
        label=(
            ""
        ),
        choices=[[1, "Own"], [2, "Rent"]],
        widget=widgets.RadioSelectHorizontal
    )
    rent_amount = models.IntegerField(
        label=(
            ""
        ),
        choices=[
            [1, "$0–$399"],
            [2, "$400–$499"],
            [3, "$500–$649"],
            [4, "$650–$799"],
            [5, "$800–$949"],
            [6, "$950–$1,099"],
            [7, "$1,100–$1,299"],
            [8, "$1,300–$1,499"],
            [9, "$1,500–$2,499"],
            [10, "$2,500 –$2,999"],
            [11, "$3,000 or more"],
        ],
        blank=True
    )

    home_value = models.IntegerField(
        label=(
            ""
        ),
        choices=[
            [1, "$0–$49,999"],
            [2, "$50,000–$99,999"],
            [3, "$100,000–$149,999"],
            [4, "$150,000–$199,999"],
            [5, "$200,000–$249,999"],
            [6, "$250,000–$299,999"],
            [7, "$300,000–$349,999"],
            [8, "$350,000–$449,999"],
            [9, "$450,000–$649,999"],
            [10, "$650,000 or more"],
        ],
        blank = True
    )
    household_income_bracket = models.IntegerField(
        label="",

        choices=[[1, "Less than 15.000"], [2, "Between 15.000 and 25.000"], [3, "Between 25.000 and 50.000"],
                 [4, "Between 50.000 and 75.000"], [5, "Between 75.000 and 100.000"], [6, "Between 100.000 and 150.000"],
                 [7, "Between 150.000 and 200.000"], [8, "More than 200.000"]],
        blank=True
    )

    household_income_exact = models.FloatField(blank=True,
                                               label="")

    # covid stimulus

    received_stimulus = models.IntegerField(
        label="",
        choices=[
            [1, "Yes"],
            [2, "No"]
        ],
        widget=widgets.RadioSelect
    )

    stimulus_amount = models.IntegerField(
        label="",
        blank=True
    )



    # --- Page 3: Household financial questions ---

    financial_decision_making = models.IntegerField(
        label="",
        choices=[
            [1, "I make all the decisions"],
            [2, "I make most of the decisions"],
            [3, "Decisions are shared equally between me and someone else"],
            [4, "Someone else makes most of the decisions"],
            [5, "Someone else makes all the decisions"],
        ],
        widget=widgets.RadioSelect
    )

    #financial_awareness = models.IntegerField(
        #label=" ",
       # choices=[[1, "Not at all informed"], [2, "Somewhat informed"], [3, "Very informed"],
                 #[4, "Extremely informed"]],
        #widget=widgets.RadioSelect
    #)

   # grocery_shopping = models.IntegerField(
      #  label="",
      #  choices=[[1, "I did the shopping alone "], [2, "I did the shopping with someone else"], [3, "Someone else did the shopping without me"]],
      #  widget=widgets.RadioSelect
   # )

   # major_purchase = models.IntegerField(
      #  label="",
      #  choices=[[1, "I made the purchase alone"], [2, "I made the purchase with someone else"], [3, "Someone else made the purchase without me"]],
       # widget=widgets.RadioSelect
  #  )


    fico_score = models.IntegerField(
        label="",
        choices=[[1, "579 or lower"], [2, "580–669"], [3, "670–739"], [4, "740–799"], [5, "800 or higher"]],
        widget=widgets.RadioSelect
    )

    bill_payment_ability = models.IntegerField(
        label="",
        choices=[
            [1, "Always"],
            [2, "Often"],
            [3, "Sometimes"],
            [4, "Rarely"],
            [5, "Never"],
        ],
        widget=widgets.RadioSelect
    )

    credit_card_payment = models.IntegerField(
        label="",
        choices=[
            [2, "Always (every month)"],
            [3, "Often (10 or 11 months per year)"],
            [4, "Sometimes (6 to 9 months per year)"],
            [5, "Rarely (1 to 5 months per year)"],
            [6, "Never (0 months per year)"],
            [1, "No credit cards or revolving credit"],
        ],
        widget=widgets.RadioSelect
    )

    credit_card_fraction_repaid = models.IntegerField(
        label="",
        min=0,
        blank=True,
    )

    installment_payment = models.IntegerField(
        label="",
        choices=[
            [2, "Always"],
            [3, "Often"],
            [4, "Sometimes"],
            [5, "Rarely"],
            [6, "Never"],
            [1, "No installment loans"],
        ],
        widget=widgets.RadioSelect
    )

    payday_payment = models.IntegerField(
        label="",
        choices=[
            [2, "Always"],
            [3, "Often"],
            [4, "Sometimes"],
            [5, "Rarely"],
            [6, "Never"],
            [1, "No payday or short-term loans"],
        ],
        widget=widgets.RadioSelect
    )


    # --- Attention Check 1 ---
    attention1 = models.IntegerField(
        label="",
        choices=[[1, "Strongly disagree"], [2, "Disagree"], [3, "Neither agree nor disagree"] ,[4, "Agree"], [5, "Strongly agree"]],
        widget=widgets.RadioSelect,
    )

# FUNCTIONS

def creating_session(subsession: Subsession):
    subsession.Treatment = subsession.session.config['Treatment']

def gender(player):
    player.participant.gender = player.gender

def prolific_id(player):
    player.participant.prolific_id = player.prolific_id

def covid_stimulus(player):

    if player.received_stimulus==2:
        player.participant.received_stimulus=2
        player.participant.stimulus_amount = 0
    elif player.received_stimulus==1:
        player.participant.received_stimulus = 1
        player.participant.stimulus_amount=player.stimulus_amount


# PAGES

class Instructions(Page):
    form_model = 'player'
    form_fields = ['prolific_id','consent']

    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.Treatment < 3 or player.subsession.Treatment in [4, 5]

    @staticmethod
    def vars_for_template(player: Player):
        return dict(is_t4=player.subsession.Treatment == 4)

    def before_next_page(player, timeout_happened):
        prolific_id(player)


class InstructionsT2(Page):
    form_model = 'player'
    form_fields = ['prolific_id','consent']

    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.Treatment == 3

    def before_next_page(player, timeout_happened):
        prolific_id(player)

class InstructionsPart1(Page):
    form_model = 'player'


class Page1(Page):
    form_model = 'player'
    form_fields = ['gender','education','marital_status','zip_code','employment_status', 'occupation_employed','occupation_unemployed',
                'occupation_employed_text','occupation_unemployed_text',
                'job_flexibility_hours','job_flexibility_overtime','patience_scale','risk_scale' ]

    @staticmethod
    def vars_for_template(player: Player):
        return dict(is_t5=player.subsession.Treatment == 5)

    def before_next_page(player, timeout_happened):
        gender(player)

    def error_message(player, values):
        def has_three_letters(text):
            return sum(char.isalpha() for char in (text or "")) >= 3

        if player.subsession.Treatment == 5:
            status = values.get('employment_status')
            if status in [1, 2, 3] and not has_three_letters(values.get('occupation_employed_text')):
                return "Please type in your main occupation."
            if status in [4, 6, 7] and not has_three_letters(values.get('occupation_unemployed_text')):
                return "Please type in your most recent main occupation."

        if values['risk_scale'] is None:
            return "Please select a value before continuing."
        if values['patience_scale'] is None:
            return "Please select a value before continuing."

class Page2(Page):
    form_model = 'player'
    form_fields = ['household_size','household_children', 'residence_owner', 'rent_amount', 'home_value', 'household_income_bracket','household_income_exact', 'received_stimulus','stimulus_amount'  ]

    def error_message(self, values):
        if values['residence_owner'] == 2 and values['rent_amount'] is None:
            return "Please provide your monthly rent."

        if values['residence_owner'] == 1 and values['home_value'] is None:
            return "Please provide the value of your home."

        if values['household_income_bracket'] is None:
            return "Please select your household income bracket."

        income = values['household_income_exact']
        bracket = values['household_income_bracket']
        if income is not None:
            if income < 0:
                return "Please enter a positive amount for your household income."

            income_ranges = {
                1: (0, 15000, False),
                2: (15000, 25000, True),
                3: (25000, 50000, True),
                4: (50000, 75000, True),
                5: (75000, 100000, True),
                6: (100000, 150000, True),
                7: (150000, 200000, True),
                8: (200000, None, False),
            }
            lower, upper, include_upper = income_ranges[bracket]
            fits_lower = income >= lower
            fits_upper = True if upper is None else (income <= upper if include_upper else income < upper)

            if not (fits_lower and fits_upper):
                return (
                    "The precise income you entered in Question 5 does not fit "
                    "the income bracket you selected in Question 4. Please update "
                    "either the bracket or the amount."
                )


    def before_next_page(player, timeout_happened):
        covid_stimulus(player)




class Page3(Page):
    form_model = 'player'
    form_fields = [
        'financial_decision_making',


        # ---- Remaining fields ----
        'fico_score',
        'bill_payment_ability',
        'credit_card_payment',
        'credit_card_fraction_repaid',
        'installment_payment',
        'payday_payment',
        'attention1'
    ]

    def error_message(player, values):
        credit_card_payment = values.get('credit_card_payment')
        fraction = values.get('credit_card_fraction_repaid')

        if credit_card_payment in [3, 4, 5, 6]:
            if fraction is None:
                return "Please enter the fraction of the amount due that your household typically pays."
            if fraction > 99:
                return (
                    "Please enter a number below 100. Since you indicated that your household "
                    "does not always pay the full amount due, this fraction should be less than 100%."
                )

    def before_next_page(player, timeout_happened):
        if player.credit_card_payment not in [3, 4, 5, 6]:
            player.credit_card_fraction_repaid = None




page_sequence = [Instructions, InstructionsT2,  Page1, Page2,Page3]
#page_sequence = [ Page1, Page2]
