from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Part2'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    Treatment = models.IntegerField()

class Group(BaseGroup):
    pass


class Player(BasePlayer):

    spending = models.IntegerField(min=-1500, max=1500)
    asset = models.IntegerField(min=-1500, max=1500)
    debt_repay = models.IntegerField(min=-1500, max=1500)
    debt_new = models.IntegerField(min=-1500, max=1500)
    labor = models.IntegerField(min=-1500, max=1500)
    q1_received_stimulus = models.IntegerField(
        label="Have you and your household ever received a Covid Stimulus check?",
        choices=[
            [1, "Yes"],
            [2, "No"]
        ],
        widget=widgets.RadioSelect
    )

    q2_amount = models.IntegerField(
        label="What was the approximate amount of the last Covid stimulus check that you and your household received?",
        blank=True
    )

    # DEBT CATEGORIES

    revolving_credit_new = models.IntegerField(
        label="Revolving credit card debt ", min=0, blank=True
    )
    mortgage_new = models.IntegerField(
        label="Mortgages ", min=0, blank=True
    )
    student_loans_new = models.IntegerField(
        label="Student loans ", min=0, blank=True
    )
    auto_loans_new = models.IntegerField(
        label="Auto loans ", min=0, blank=True
    )
    other_loans_new = models.IntegerField(
        label="Other loans ", min=0, blank=True
    )
    unpaid_bills_new = models.IntegerField(
        label="Unpaid bills (e.g., legal, medical, utilities) ", min=0, blank=True
    )
    revolving_credit_repay = models.IntegerField(
        label="Revolving credit card debt ", min=0, blank=True
    )
    mortgage_repay = models.IntegerField(
        label="Mortgages", min=0, blank=True
    )
    student_loans_repay = models.IntegerField(
        label="Student loans ", min=0, blank=True
    )
    auto_loans_repay = models.IntegerField(
        label="Auto loans", min=0, blank=True
    )
    other_loans_repay = models.IntegerField(
        label="Other loans", min=0, blank=True
    )
    unpaid_bills_repay = models.IntegerField(
        label="Unpaid bills (e.g., legal, medical, utilities)", min=0, blank=True
    )

    # 0–10 integer scales
    understanding_difficulty = models.IntegerField(
        label="",choices=[0,1,2,3,4,5,6,7,8,9,10],
        widget=widgets.RadioSelectHorizontal
    )

    mental_effort = models.IntegerField(
        label="",
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        widget=widgets.RadioSelectHorizontal
    )

    # Category coverage question
    categories_cover = models.IntegerField(
        label="",
        choices=[
            [0, "Yes, all of my uses fit the categories"],
            [1, "No"],
        ],
        widget=widgets.RadioSelect
    )

    categories_specify = models.LongStringField(
        label="Please specify:",
        blank=True
    )
    #Scenarios

    spending_Robin = models.IntegerField(min=-1500, max=1500)
    asset_Robin = models.IntegerField(min=-1500, max=1500)
    debt_repay_Robin = models.IntegerField(min=-1500, max=1500)
    debt_new_Robin = models.IntegerField(min=-1500, max=1500)
    labor_Robin = models.IntegerField(min=-1500, max=1500)
    spending_Taylor = models.IntegerField(min=-10000, max=10000)
    asset_Taylor = models.IntegerField(min=-10000, max=10000)
    debt_repay_Taylor = models.IntegerField(min=-10000, max=10000)
    debt_new_Taylor = models.IntegerField(min=-10000, max=10000)
    labor_Taylor = models.IntegerField(min=-10000, max=10000)
    spending_Charlie = models.IntegerField(min=-1500, max=1500)
    asset_Charlie = models.IntegerField(min=-1500, max=1500)
    debt_repay_Charlie = models.IntegerField(min=-1500, max=1500)
    debt_new_Charlie = models.IntegerField(min=-1500, max=1500)
    labor_Charlie = models.IntegerField(min=-1500, max=1500)
    categories_cover_scenario = models.IntegerField(
        label="",
        choices=[
            [0, "Yes, all of their uses fit the categories"],
            [1, "No"],
        ],
        widget=widgets.RadioSelect
    )

    categories_specify_scenario = models.LongStringField(
        label="Please specify:",
        blank=True
    )

    payment_intended_for = models.IntegerField(
        label="",
        choices=[[1, "For me personally"],
            [2, "For the entire household (joint money)"],[3,"Not sure"]],
        widget=widgets.RadioSelect,
    )

    payment_access = models.StringField(
        label="",
        choices=[
            [1,"Only me"],
            [2,"Me and other household members"],
            [3,"Not sure"]],
        widget=widgets.RadioSelect,
    )

    payment_different_if_personal = models.StringField(
        label="",
        choices=[
            "Yes",
            "No",
            "Not sure",
        ],
        widget=widgets.RadioSelect,
    )

    payment_different_explain = models.LongStringField(
        label="<b> How would your answers have changed? Please explain: </b>",
        blank=True,
    )

    deposit_account = models.IntegerField(
        label="",
        choices=[
            [1, "On an account to which only I have access"],
            [2, "On a joint account shared with other household members"],
            [3, "On an account to which I do not have access"],
            [4, "Not sure"],
        ],
        widget=widgets.RadioSelect
    )


# FUNCTIONS

def creating_session(subsession: Subsession):
    subsession.Treatment = subsession.session.config['Treatment']

def amount_stimulus(player):

    if player.q1_received_stimulus==2:
        player.participant.q2_amount = 0
    elif player.q1_received_stimulus==1:
         player.participant.q2_amount=player.q2_amount

def debt(player):

    player.participant.debt_new = player.debt_new
    player.participant.debt_repay = player.debt_repay

def debtBaseline(player):
    player.participant.debt_repay = player.debt_repay


# PAGES
class instructionsT0(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.Treatment == 1


class instructionsT1(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.Treatment == 2 or player.subsession.Treatment == 3 and player.q1_received_stimulus==2

class instructionsT2(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return  player.subsession.Treatment == 3 and player.q1_received_stimulus==1


class questionCovid(Page):
    form_model = 'player'
    form_fields = ['q1_received_stimulus', 'q2_amount']

    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.Treatment == 3

    def before_next_page(player, timeout_happened):
        amount_stimulus(player)

class ElicitationT0(Page):
    form_model = 'player'
    form_fields = [
        'spending',
        'debt_repay'
    ]

    @staticmethod
    def is_displayed(player: Player):
        return  player.subsession.Treatment == 1

    def before_next_page(player, timeout_happened):
        debtBaseline(player)


class ElicitationT1(Page):
    form_model = 'player'
    form_fields = [
        'spending',
        'asset',
        'debt_repay',
        'debt_new',
        'labor',
    ]


    @staticmethod
    def is_displayed(player: Player):
        return  player.subsession.Treatment == 2 or player.subsession.Treatment == 3 and player.q1_received_stimulus ==2

    def before_next_page(player, timeout_happened):
        debt(player)

class ElicitationT2(Page):
    form_model = 'player'
    form_fields = [
        'spending',
        'asset',
        'debt_repay',
        'debt_new',
        'labor']
    @staticmethod
    def is_displayed(player: Player):
        return  player.subsession.Treatment == 3 and player.q1_received_stimulus ==1

    def before_next_page(player, timeout_happened):
        debt(player)

class QuestionsDebtRepay(Page):
    form_model = 'player'
    form_fields = [
        'revolving_credit_repay',
        'mortgage_repay',
        'student_loans_repay',
        'auto_loans_repay',
        'other_loans_repay',
        'unpaid_bills_repay',
    ]

    def vars_for_template(player: Player):
        return dict(
            repay_debt=player.debt_repay,
            abs_repay_debt=abs(player.debt_repay or 0),
        )

    def error_message(player: Player, values):
        repay_debt = player.debt_repay or 0
        abs_debt = abs(repay_debt)

        total_alloc = sum([
            values['revolving_credit_repay'] or 0,
            values['mortgage_repay'] or 0,
            values['student_loans_repay'] or 0,
            values['auto_loans_repay'] or 0,
            values['other_loans_repay'] or 0,
            values['unpaid_bills_repay'] or 0,
        ])

        # Allow small rounding error
        if abs(total_alloc - abs_debt) > 0.01:
            return f"The total allocation (${int(total_alloc)}) must equal ${int(abs_debt)}."

    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.Treatment == 1 and player.participant.debt_repay!=0 or player.subsession.Treatment == 2 and player.participant.debt_repay!=0 or player.subsession.Treatment==3 and player.q1_received_stimulus ==2 and player.participant.debt_repay!=0

class QuestionsDebtRepayT2(Page):
    form_model = 'player'
    form_fields = [
        'revolving_credit_repay',
        'mortgage_repay',
        'student_loans_repay',
        'auto_loans_repay',
        'other_loans_repay',
        'unpaid_bills_repay',
    ]

    def vars_for_template(player: Player):
        return dict(
            repay_debt=player.debt_repay,
            abs_repay_debt=abs(player.debt_repay or 0),
        )

    def error_message(player: Player, values):
        repay_debt = player.debt_repay or 0
        abs_debt = abs(repay_debt)

        total_alloc = sum([
            values['revolving_credit_repay'] or 0,
            values['mortgage_repay'] or 0,
            values['student_loans_repay'] or 0,
            values['auto_loans_repay'] or 0,
            values['other_loans_repay'] or 0,
            values['unpaid_bills_repay'] or 0,
        ])

        # Allow small rounding error
        if abs(total_alloc - abs_debt) > 0.01:
            return f"The total allocation (${int(total_alloc)}) must equal ${int(abs_debt)}."

    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.Treatment==3 and player.q1_received_stimulus ==1 and player.participant.debt_repay!=0






class QuestionsDebtNew(Page):
    form_model = 'player'
    form_fields = [
        'revolving_credit_new',
        'mortgage_new',
        'student_loans_new',
        'auto_loans_new',
        'other_loans_new',
        'unpaid_bills_new',
    ]

    def vars_for_template(player: Player):
        return dict(
            new_debt=player.debt_new,
            abs_new_debt=abs(player.debt_new or 0),
        )

    def error_message(player: Player, values):
        new_debt = player.participant.debt_new or 0
        abs_debt = abs(player.participant.debt_new)

        total_alloc = sum([
            values['revolving_credit_new'] or 0,
            values['mortgage_new'] or 0,
            values['student_loans_new'] or 0,
            values['auto_loans_new'] or 0,
            values['other_loans_new'] or 0,
            values['unpaid_bills_new'] or 0,
        ])

        # Allow small rounding error
        if abs(total_alloc - abs_debt) > 0.01:
            return f"The total allocation (${int(total_alloc)}) must equal ${int(abs_debt)}."

    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.Treatment == 2 and player.participant.debt_new!=0 or player.subsession.Treatment==3 and player.q1_received_stimulus ==2 and player.participant.debt_new!=0

class QuestionsDebtNewT2(Page):
    form_model = 'player'
    form_fields = [
        'revolving_credit_new',
        'mortgage_new',
        'student_loans_new',
        'auto_loans_new',
        'other_loans_new',
        'unpaid_bills_new',
    ]

    def vars_for_template(player: Player):
        return dict(
            new_debt=player.debt_new,
            abs_new_debt=abs(player.debt_new or 0),
        )

    def error_message(player: Player, values):
        new_debt = player.participant.debt_new or 0
        abs_debt = abs(player.participant.debt_new)

        total_alloc = sum([
            values['revolving_credit_new'] or 0,
            values['mortgage_new'] or 0,
            values['student_loans_new'] or 0,
            values['auto_loans_new'] or 0,
            values['other_loans_new'] or 0,
            values['unpaid_bills_new'] or 0,
        ])

        # Allow small rounding error
        if abs(total_alloc - abs_debt) > 0.01:
            return f"The total allocation (${int(total_alloc)}) must equal ${int(abs_debt)}."

    @staticmethod
    def is_displayed(player: Player):
        return  player.subsession.Treatment==3 and player.q1_received_stimulus ==1  and player.participant.debt_new!=0


class FeedbackElicitation(Page):
    form_model = 'player'
    form_fields = [
        'understanding_difficulty',
        'mental_effort',
        'categories_cover',
        'categories_specify',
    ]

class InstructionsScenarios(Page):
    form_model = 'player'



class Robin(Page):
    form_model = 'player'
    form_fields = [
        'spending_Robin',
        'asset_Robin',
        'debt_repay_Robin',
        'debt_new_Robin',
        'labor_Robin',
    ]

    def vars_for_template(player: Player):
        gender = player.participant.gender
        if gender == 1:
            pronoun_subject = "he"
            pronoun_object = "his"
        elif gender == 2:
            pronoun_subject = "she"
            pronoun_object = "her"
        else:
            pronoun_subject = "they"
            pronoun_object = "their"

        return dict(
            pronoun_subject=pronoun_subject,
            pronoun_object=pronoun_object,
        )

    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.Treatment == 2 or player.subsession.Treatment == 3

class RobinT0(Page):
    form_model = 'player'
    form_fields = [
        'spending_Robin',
        'debt_repay_Robin',
    ]

    def vars_for_template(player: Player):
        gender = player.participant.gender
        if gender == 1:
            pronoun_subject = "he"
            pronoun_object = "his"
        elif gender == 2:
            pronoun_subject = "she"
            pronoun_object = "her"
        else:
            pronoun_subject = "they"
            pronoun_object = "their"

        return dict(
            pronoun_subject=pronoun_subject,
            pronoun_object=pronoun_object,
        )

    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.Treatment == 1

class TaylorT0(Page):
    form_model = 'player'
    form_fields = [
        'spending_Taylor',
        'debt_repay_Taylor',
    ]

    def vars_for_template(player: Player):
        gender = player.participant.gender
        if gender == 1:
            pronoun_subject = "he"
            pronoun_object = "his"
        elif gender == 2:
            pronoun_subject = "she"
            pronoun_object = "her"
        else:
            pronoun_subject = "they"
            pronoun_object = "their"

        return dict(
            pronoun_subject=pronoun_subject,
            pronoun_object=pronoun_object,
        )

    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.Treatment == 1


class Taylor(Page):
    form_model = 'player'
    form_fields = [
        'spending_Taylor',
        'asset_Taylor',
        'debt_repay_Taylor',
        'debt_new_Taylor',
        'labor_Taylor',
    ]

    def vars_for_template(player: Player):
        gender = player.participant.gender
        if gender == 1:
            pronoun_subject = "he"
            pronoun_object = "his"
        elif gender == 2:
            pronoun_subject = "she"
            pronoun_object = "her"
        else:
            pronoun_subject = "they"
            pronoun_object = "their"

        return dict(
            pronoun_subject=pronoun_subject,
            pronoun_object=pronoun_object,
        )

    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.Treatment == 2 or player.subsession.Treatment == 3

class Charlie(Page):
    form_model = 'player'
    form_fields = [
        'spending_Charlie',
        'asset_Charlie',
        'debt_repay_Charlie',
        'debt_new_Charlie',
        'labor_Charlie',
    ]

    def vars_for_template(player: Player):
        gender = player.participant.gender
        if gender == 1:
            pronoun_subject = "he"
            pronoun_object = "his"
        elif gender == 2:
            pronoun_subject = "she"
            pronoun_object = "her"
        else:
            pronoun_subject = "they"
            pronoun_object = "their"

        return dict(
            pronoun_subject=pronoun_subject,
            pronoun_object=pronoun_object,
        )

    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.Treatment == 2 or player.subsession.Treatment == 3

class CharlieT0(Page):
    form_model = 'player'
    form_fields = [
        'spending_Charlie',
        'debt_repay_Charlie',
    ]

    def vars_for_template(player: Player):
        gender = player.participant.gender
        if gender == 1:
            pronoun_subject = "he"
            pronoun_object = "his"
        elif gender == 2:
            pronoun_subject = "she"
            pronoun_object = "her"
        else:
            pronoun_subject = "they"
            pronoun_object = "their"

        return dict(
            pronoun_subject=pronoun_subject,
            pronoun_object=pronoun_object,
        )

    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.Treatment == 1



class FeedbackScenario(Page):
    form_model = 'player'
    form_fields = [
        'categories_cover_scenario',
        'categories_specify_scenario',
    ]


class PaymentInterpretation(Page):
    form_model = 'player'
    form_fields = [
        'payment_intended_for',
        'payment_access',
        'payment_different_if_personal',
        'payment_different_explain',
    ]

    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.Treatment == 1 or player.subsession.Treatment == 2
class PaymentInterpretationT2(Page):
    form_model = 'player'
    form_fields = [
        'deposit_account',
        'payment_different_if_personal',
        'payment_different_explain',
    ]

    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.Treatment == 3
class End(Page):
    form_model = 'player'



page_sequence = [questionCovid, instructionsT0, instructionsT1,  instructionsT2, ElicitationT0,ElicitationT1, ElicitationT2, FeedbackElicitation ,QuestionsDebtRepay,QuestionsDebtRepayT2, QuestionsDebtNew, QuestionsDebtNewT2, InstructionsScenarios, Robin, RobinT0, Taylor, TaylorT0, Charlie, CharlieT0, FeedbackScenario, PaymentInterpretation,PaymentInterpretationT2,End]
