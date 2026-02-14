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
# ================= SPENDING =================

    spend_increase = models.StringField(
        choices=[('yes', 'Yes'), ('no', 'No')],
        widget=widgets.RadioSelect
    )
    spend_same_or_decrease = models.StringField(
        choices=[('same', 'Keep the same'), ('decrease', 'Decrease')],
        widget=widgets.RadioSelect,
        blank=True
    )
    spend_amount = models.CurrencyField(blank=True)

    spend_everyday = models.CurrencyField(blank=True)
    spend_leisure = models.CurrencyField(blank=True)
    spend_services = models.CurrencyField(blank=True)
    spend_durable = models.CurrencyField(blank=True)

    # ================= DEBT REPAYMENT =================
    debt_increase = models.StringField(
        choices=[('yes', 'Yes'), ('no', 'No')],
        widget=widgets.RadioSelect
    )
    debt_same_or_decrease = models.StringField(
        choices=[('same', 'Keep the same'), ('decrease', 'Decrease')],
        widget=widgets.RadioSelect,
        blank=True
    )
    debt_amount = models.CurrencyField(blank=True)

    debt_cc = models.CurrencyField(blank=True)
    debt_bills = models.CurrencyField(blank=True)
    debt_short = models.CurrencyField(blank=True)
    debt_long = models.CurrencyField(blank=True)

    # ================= LABOR =================
    labor_decrease = models.StringField(
        choices=[('yes', 'Yes'), ('no', 'No')],
        widget=widgets.RadioSelect
    )
    labor_same_or_increase = models.StringField(
        choices=[('same', 'Keep the same'), ('increase', 'Increase')],
        widget=widgets.RadioSelect,
        blank=True
    )
    labor_hours = models.FloatField(blank=True)
    labor_income = models.CurrencyField(blank=True)

    labor_gigs = models.CurrencyField(blank=True)
    labor_overtime = models.CurrencyField(blank=True)
    labor_holidays = models.CurrencyField(blank=True)
    labor_contract = models.CurrencyField(blank=True)

    # ================= NEW DEBT =================
    newdebt_same_or_decrease = models.StringField(
    choices=[('same', 'Keep the same'), ('decrease', 'Decrease')],
    widget=widgets.RadioSelect
    )

    newdebt_increase = models.StringField(
        choices=[('yes', 'Yes'), ('no', 'No')],
        widget=widgets.RadioSelect
    )
    newdebt_amount = models.CurrencyField(blank=True)

    newdebt_cc = models.CurrencyField(blank=True)
    newdebt_bills = models.CurrencyField(blank=True)
    newdebt_short = models.CurrencyField(blank=True)
    newdebt_long = models.CurrencyField(blank=True)

    # ================= SAVINGS =================
    save_increase = models.StringField(
        choices=[('yes', 'Yes'), ('no', 'No')],
        widget=widgets.RadioSelect
    )
    save_same_or_decrease = models.StringField(
        choices=[('same', 'Keep the same'), ('decrease', 'Decrease')],
        widget=widgets.RadioSelect,
        blank=True
    )
    save_amount = models.CurrencyField(blank=True)

    save_accounts = models.CurrencyField(blank=True)
    save_lowrisk = models.CurrencyField(blank=True)
    save_risky = models.CurrencyField(blank=True)
    save_realestate = models.CurrencyField(blank=True)
    save_business = models.CurrencyField(blank=True)
    save_crypto = models.CurrencyField(blank=True)
###

    spend_increase = models.StringField(
        choices=[('yes', 'Yes'), ('no', 'No')],
        widget=widgets.RadioSelect
    )

    spend_increase_amount = models.CurrencyField(min=0, blank=True)

    spend_same_or_decrease = models.StringField(
        choices=[('same', 'Keep the same'), ('decrease', 'Decrease my spending')],
        widget=widgets.RadioSelect,
        blank=True
    )

    spend_decrease_amount = models.CurrencyField(min=0, blank=True)

    spend_nondurable = models.CurrencyField(min=0, blank=True)
    spend_services = models.CurrencyField(min=0, blank=True)
    spend_durable = models.CurrencyField(min=0, blank=True)
    spend_other = models.CurrencyField(min=0, blank=True)
    spend_other_text = models.LongStringField(blank=True)

    spend_debt = models.StringField(
        choices=[('yes', 'Yes'), ('no', 'No')],
        widget=widgets.RadioSelect,
        blank=True
    )

    debt_repay_increase = models.StringField(
        choices=[('yes', 'Yes'), ('no', 'No')],
        widget=widgets.RadioSelect
    )

    ## Debt Repayment ##

    debt_repay_increase_amount = models.CurrencyField(min=0, blank=True)

    debt_repay_same_or_decrease = models.StringField(
        choices=[('same', 'Keep the same'), ('decrease', 'Decrease my repayment')],
        widget=widgets.RadioSelect,
        blank=True
    )

    debt_repay_decrease_amount = models.CurrencyField(min=0, blank=True)

    debt_cc = models.CurrencyField(min=0, blank=True)
    debt_bills = models.CurrencyField(min=0, blank=True)
    debt_payday = models.CurrencyField(min=0, blank=True)
    debt_longterm = models.CurrencyField(min=0, blank=True)
    debt_other = models.CurrencyField(min=0, blank=True)
    debt_other_text = models.LongStringField(blank=True)

    # LABOR

    labor_decrease = models.StringField(
        choices=[('yes', 'Yes'), ('no', 'No')],
        widget=widgets.RadioSelect
    )

    labor_income_decrease_amount = models.CurrencyField(min=0, blank=True)

    labor_same_or_increase = models.StringField(
        choices=[('same', 'Keep the same'), ('increase', 'Increase working time')],
        widget=widgets.RadioSelect,
        blank=True
    )

    labor_income_increase_amount = models.CurrencyField(min=0, blank=True)

    labor_gigs = models.CurrencyField(min=0, blank=True)
    labor_overtime = models.CurrencyField(min=0, blank=True)
    labor_holidays = models.CurrencyField(min=0, blank=True)
    labor_contract = models.CurrencyField(min=0, blank=True)
    labor_other = models.CurrencyField(min=0, blank=True)
    labor_other_text = models.LongStringField(blank=True)

    # NEW DEBT

    new_debt_increase = models.StringField(
        choices=[('yes', 'Yes'), ('no', 'No')],
        widget=widgets.RadioSelect
    )

    new_debt_increase_amount = models.CurrencyField(min=0, blank=True)

    new_debt_same_or_decrease = models.StringField(
        choices=[('same', 'Keep the same'), ('decrease', 'Decrease new debt')],
        widget=widgets.RadioSelect,
        blank=True
    )

    new_debt_decrease_amount = models.CurrencyField(min=0, blank=True)

    new_debt_cc = models.CurrencyField(min=0, blank=True)
    new_debt_bills = models.CurrencyField(min=0, blank=True)
    new_debt_payday = models.CurrencyField(min=0, blank=True)
    new_debt_auto = models.CurrencyField(min=0, blank=True)
    new_debt_student = models.CurrencyField(min=0, blank=True)
    new_debt_mortgage = models.CurrencyField(min=0, blank=True)
    new_debt_other = models.CurrencyField(min=0, blank=True)
    new_debt_other_text = models.LongStringField(blank=True)

    # ======================================================
    # SAVINGS AND INVESTMENTS
    # ======================================================

    save_invest_increase = models.StringField(
        choices=[('yes', 'Yes'), ('no', 'No')],
        widget=widgets.RadioSelect
    )

    save_invest_increase_amount = models.CurrencyField(min=0, blank=True)

    save_invest_same_or_decrease = models.StringField(
        choices=[('same', 'Keep the same'), ('decrease', 'Decrease')],
        widget=widgets.RadioSelect,
        blank=True
    )

    save_invest_decrease_amount = models.CurrencyField(min=0, blank=True)

    # Allocation categories
    save_accounts = models.CurrencyField(min=0, blank=True)
    save_lowrisk = models.CurrencyField(min=0, blank=True)
    save_stocks = models.CurrencyField(min=0, blank=True)
    save_realestate = models.CurrencyField(min=0, blank=True)
    save_business = models.CurrencyField(min=0, blank=True)
    save_crypto = models.CurrencyField(min=0, blank=True)
    save_other = models.CurrencyField(min=0, blank=True)
    save_other_text = models.LongStringField(blank=True)

    # ======================================================
    # REVIEW / REVISION PAGE
    # ======================================================

    # Final (possibly revised) answers
    spending_final = models.CurrencyField(blank=True)
    debt_repay_final = models.CurrencyField(blank=True)
    labor_income_final = models.CurrencyField(blank=True)
    new_debt_final = models.CurrencyField(blank=True)
    save_invest_final = models.CurrencyField(blank=True)

    # Revision indicators
    revised_any = models.BooleanField(initial=False)

    # Revision reasons (multiple choice)
    revision_misunderstood = models.BooleanField(initial=False)
    revision_rethought_less = models.BooleanField(initial=False)
    revision_rethought_more = models.BooleanField(initial=False)
    revision_context = models.BooleanField(initial=False)
    revision_mistake = models.BooleanField(initial=False)
    revision_other = models.BooleanField(initial=False)

    revision_other_text = models.LongStringField(blank=True)


    spending = models.IntegerField(min=-1500, max=1500)
    asset = models.IntegerField(min=-1500, max=1500)
    debt_repay = models.IntegerField(min=-1500, max=1500)
    debt_new = models.IntegerField(min=-1500, max=1500)
    labor = models.IntegerField(min=-1500, max=1500)




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
    attention2 = models.IntegerField(
        label="",
        choices=[[1, "Not at all concerned"],
                 [2, "Slightly concerned"],[3, "Moderately concerned"],[4, "Very concerned"],[5, "Extremely concerned"]],
        widget=widgets.RadioSelectHorizontal,
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
    correct_Robin=models.BooleanField()
    correct_RobinT0 = models.BooleanField()
    spending_Taylor = models.IntegerField(min=-10000, max=10000)
    asset_Taylor = models.IntegerField(min=-10000, max=10000)
    debt_repay_Taylor = models.IntegerField(min=-10000, max=10000)
    debt_new_Taylor = models.IntegerField(min=-10000, max=10000)
    labor_Taylor = models.IntegerField(min=-10000, max=10000)
    correct_Taylor = models.BooleanField()
    correct_TaylorT0 = models.BooleanField()
    spending_Charlie = models.IntegerField(min=-1500, max=1500)
    asset_Charlie = models.IntegerField(min=-1500, max=1500)
    debt_repay_Charlie = models.IntegerField(min=-1500, max=1500)
    debt_new_Charlie = models.IntegerField(min=-1500, max=1500)
    labor_Charlie = models.IntegerField(min=-1500, max=1500)
    correct_Charlie = models.BooleanField()
    correct_CharlieT0 = models.BooleanField()
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
        blank=True,
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

def spending(player):
    inc = player.field_maybe_none('spend_increase_amount')
    dec = player.field_maybe_none('spend_decrease_amount')

    if inc is not None:
        value = inc
    elif dec is not None:
        value = -dec
    else:
        value = None

    player.participant.spending_net = value


def debtRepay(player):
    inc = player.field_maybe_none('debt_repay_increase_amount')
    dec = player.field_maybe_none('debt_repay_decrease_amount')

    if inc is not None:
        value = inc
    elif dec is not None:
        value = -dec
    else:
        value = None

    player.participant.debt_repay_net = value


def debtNew(player):
    inc = player.field_maybe_none('new_debt_increase_amount')
    dec = player.field_maybe_none('new_debt_decrease_amount')

    if inc is not None:
        value = inc
    elif dec is not None:
        value = -dec
    else:
        value = None

    player.participant.new_debt_net = value


def labor(player):
    inc = player.field_maybe_none('labor_income_increase_amount')
    dec = player.field_maybe_none('labor_income_decrease_amount')

    if inc is not None:
        value = inc
    elif dec is not None:
        value = -dec
    else:
        value = None

    player.participant.labor_income_net = value


def saveInvest(player):
    inc = player.field_maybe_none('save_invest_increase_amount')
    dec = player.field_maybe_none('save_invest_decrease_amount')

    if inc is not None:
        value = inc
    elif dec is not None:
        value = -dec
    else:
        value = None

    player.participant.save_invest_net = value


def debtBaseline(player):
    player.participant.debt_repay = player.debt_repay

def correct_Robin(player):

    if player.spending_Robin == 500 and player.debt_repay_Robin==200 and player.asset_Robin==0 and player.debt_new_Robin == 0 and player.labor_Robin==0:
        correct_Robin = True
    else:
        correct_Robin = False

    player.correct_Robin = correct_Robin


def correct_RobinT0(player):
    if player.spending_Robin == 500 and player.debt_repay_Robin == 200:
        correct_Robin = True
    else:
        correct_Robin = False

    player.correct_Robin = correct_Robin


def correct_Taylor(player):
    if player.spending_Taylor == 0 and player.debt_repay_Taylor == 0 and player.asset_Taylor == 8000   and player.debt_new_Taylor == 5000 and player.labor_Taylor == 0:
        correct_Taylor = True
    else:
        correct_Taylor = False

    player.correct_Taylor = correct_Taylor

def correct_TaylorT0(player):
    if player.spending_Taylor == 8000 and player.debt_repay_Taylor == 0 or player.spending_Taylor == 8000 and player.debt_repay_Taylor == -5000 or player.spending_Taylor == 0 and player.debt_repay_Taylor == -5000 or player.spending_Taylor == 0 and player.debt_repay_Taylor ==0:
        correct_Taylor = True
    else:
        correct_Taylor = False

    player.correct_Taylor = correct_Taylor

def correct_Charlie(player):
    if player.spending_Charlie == 200 and player.debt_repay_Charlie == 600 and player.asset_Charlie == 0   and player.debt_new_Charlie == 200 and player.labor_Charlie == 0:
        correct_Charlie = True
    else:
        correct_Charlie = False

    player.correct_Charlie = correct_Charlie

def correct_CharlieT0(player):
    if player.spending_Charlie == 200 and player.debt_repay_Charlie == 600 or player.spending_Charlie == 200 and player.debt_repay_Charlie == 400:
        correct_Charlie = True
    else:
        correct_Charlie = False

    player.correct_Charlie = correct_Charlie

def set_payoff(player):

    if player.correct_Charlie== False and player.correct_Taylor==False and player.correct_Robin== False:
        player.participant.payoff = 2
    elif player.correct_Charlie== False and player.correct_Taylor==False and player.correct_Robin== True or player.correct_Charlie== False and player.correct_Taylor==True and player.correct_Robin== False or player.correct_Charlie== True and player.correct_Taylor==False and player.correct_Robin== False:
        player.participant.payoff = 3
    elif player.correct_Charlie== False and player.correct_Taylor==True and player.correct_Robin== True or player.correct_Charlie== True and player.correct_Taylor==True and player.correct_Robin== False or player.correct_Charlie== True and player.correct_Taylor==False and player.correct_Robin== True:
        player.participant.payoff = 4
    elif player.correct_Charlie== True and player.correct_Taylor==True and player.correct_Robin== True:
        player.participant.payoff = 5

def set_payoff_questions(player):

    points=player.participant.payoff - 2

    player.participant.payoff_questions=points




    # PAGES

class InstructionsPart2(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.Treatment <3 or player.subsession.Treatment == 3 and player.participant.received_stimulus == 2


class InstructionsPart2T2(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.Treatment == 3 and player.participant.received_stimulus == 1


class instructionsT0(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.Treatment == 1


class instructionsT1(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.Treatment == 2 or player.subsession.Treatment == 3 and player.participant.received_stimulus==2

class instructionsT2(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return  player.subsession.Treatment == 3 and player.participant.received_stimulus==1


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

class Spending(Page):
    form_model = 'player'
    form_fields = [
        'spend_increase',
        'spend_increase_amount',
        'spend_same_or_decrease',
        'spend_decrease_amount',
        'spend_nondurable',
        'spend_services',
        'spend_durable',
        'spend_other',
        'spend_other_text',
        'spend_debt',
    ]

    def error_message(self, values):

        # --- Determine reported total change ---
        if values['spend_increase'] == 'yes':
            reported_amount = values['spend_increase_amount']
        elif values['spend_same_or_decrease'] == 'decrease':
            reported_amount = values['spend_decrease_amount']
        else:
            reported_amount = None

        # --- Allocation check only if there is a change ---
        if reported_amount is not None:

            allocation_fields = [
                values['spend_nondurable'] or 0,
                values['spend_services'] or 0,
                values['spend_durable'] or 0,
                values['spend_other'] or 0,
            ]

            allocation_sum = sum(allocation_fields)

            if allocation_sum != reported_amount:
                return (
                    f"The amounts you entered across categories add up to "
                    f"{allocation_sum}, but you reported a total change of "
                    f"{reported_amount}. "
                    f"Please make sure the amounts match."
                )


    def before_next_page(player, timeout_happened):
        spending(player)

class DebtRepayment(Page):
    form_model = 'player'
    form_fields = [
        'debt_repay_increase',
        'debt_repay_increase_amount',
        'debt_repay_same_or_decrease',
        'debt_repay_decrease_amount',
        'debt_cc',
        'debt_bills',
        'debt_payday',
        'debt_longterm',
        'debt_other',
        'debt_other_text',
    ]

    def error_message(self, values):

        # --- determine reported total ---
        if values['debt_repay_increase'] == 'yes':
            total = values['debt_repay_increase_amount']
            if total is None:
                return "Please enter the amount by which your debt repayment would increase."

        elif values['debt_repay_same_or_decrease'] == 'decrease':
            total = values['debt_repay_decrease_amount']
            if total is None:
                return "Please enter the amount by which your debt repayment would decrease."

        else:
            total = None

        # --- allocation consistency ---
        if total is not None:
            allocation = (
                (values['debt_cc'] or 0)
                + (values['debt_bills'] or 0)
                + (values['debt_payday'] or 0)
                + (values['debt_longterm'] or 0)
                + (values['debt_other'] or 0)
            )

            if allocation != total:
                return (
                    f"The amounts allocated across debt categories add up to {allocation}, "
                    f"but you reported a total change of {total}. "
                    f"Please make sure these amounts match."
                )


    def before_next_page(player, timeout_happened):
        debtRepay(player)

class Labor(Page):
    form_model = 'player'
    form_fields = [
        'labor_decrease',
        'labor_income_decrease_amount',
        'labor_same_or_increase',
        'labor_income_increase_amount',
        'labor_gigs',
        'labor_overtime',
        'labor_holidays',
        'labor_contract',
        'labor_other',
        'labor_other_text',
    ]

    def error_message(self, values):

        if values['labor_decrease'] == 'yes':
            total = values['labor_income_decrease_amount']
            if total is None:
                return "Please enter the decrease in your labor income."

        elif values['labor_same_or_increase'] == 'increase':
            total = values['labor_income_increase_amount']
            if total is None:
                return "Please enter the increase in your labor income."

        else:
            total = None

        if total is not None:
            allocation = (
                (values['labor_gigs'] or 0)
                + (values['labor_overtime'] or 0)
                + (values['labor_holidays'] or 0)
                + (values['labor_contract'] or 0)
                + (values['labor_other'] or 0)
            )

            if allocation != total:
                return (
                    f"The amounts across categories add up to {allocation}, "
                    f"but you reported a total change of {total}. "
                    f"Please make sure these amounts match."
                )


    def before_next_page(player, timeout_happened):
        labor(player)
class NewDebt(Page):
    form_model = 'player'
    form_fields = [
        'new_debt_increase',
        'new_debt_increase_amount',
        'new_debt_same_or_decrease',
        'new_debt_decrease_amount',
        'new_debt_cc',
        'new_debt_bills',
        'new_debt_payday',
        'new_debt_auto',
        'new_debt_student',
        'new_debt_mortgage',
        'new_debt_other',
        'new_debt_other_text',
    ]

    def error_message(self, values):

        if values['new_debt_increase'] == 'yes':
            total = values['new_debt_increase_amount']
            if total is None:
                return "Please enter the increase in new debt."

        elif values['new_debt_same_or_decrease'] == 'decrease':
            total = values['new_debt_decrease_amount']
            if total is None:
                return "Please enter the decrease in new debt."

        else:
            total = None

        if total is not None:
            allocation = (
                (values['new_debt_cc'] or 0)
                + (values['new_debt_bills'] or 0)
                + (values['new_debt_payday'] or 0)
                + (values['new_debt_auto'] or 0)
                + (values['new_debt_student'] or 0)
                + (values['new_debt_mortgage'] or 0)
                + (values['new_debt_other'] or 0)
            )

            if allocation != total:
                return (
                    f"The amounts across categories add up to {allocation}, "
                    f"but you reported a total change of {total}. "
                    f"Please make sure these amounts match."
                )


    def before_next_page(player, timeout_happened):
        debtNew(player)
class SavingsInvestments(Page):
    form_model = 'player'
    form_fields = [
        'save_invest_increase',
        'save_invest_increase_amount',
        'save_invest_same_or_decrease',
        'save_invest_decrease_amount',
        'save_accounts',
        'save_lowrisk',
        'save_stocks',
        'save_realestate',
        'save_business',
        'save_crypto',
        'save_other',
        'save_other_text',
    ]

    def error_message(self, values):

        # --- determine reported total ---
        if values['save_invest_increase'] == 'yes':
            total = values['save_invest_increase_amount']
            if total is None:
                return (
                    "Please enter the amount by which your savings or "
                    "investments would increase."
                )

        elif values['save_invest_same_or_decrease'] == 'decrease':
            total = values['save_invest_decrease_amount']
            if total is None:
                return (
                    "Please enter the amount by which your savings or "
                    "investments would decrease."
                )

        else:
            total = None

        # --- allocation consistency ---
        if total is not None:
            allocation = (
                (values['save_accounts'] or 0)
                + (values['save_lowrisk'] or 0)
                + (values['save_stocks'] or 0)
                + (values['save_realestate'] or 0)
                + (values['save_business'] or 0)
                + (values['save_crypto'] or 0)
                + (values['save_other'] or 0)
            )

            if allocation != total:
                return (
                    f"The amounts allocated across categories add up to {allocation}, "
                    f"but you reported a total change of {total}. "
                    f"Please make sure these amounts match."
                )




    def before_next_page(player, timeout_happened):
        saveInvest(player)

class Review(Page):
    form_model = 'player'
    form_fields = [
        'spending_final',
        'debt_repay_final',
        'labor_income_final',
        'new_debt_final',
        'save_invest_final',
        'revision_misunderstood',
        'revision_rethought_less',
        'revision_rethought_more',
        'revision_context',
        'revision_mistake',
        'revision_other',
        'revision_other_text',
    ]

    def vars_for_template(player):
        p = player.participant

        def safe(x):
            return x if x is not None else 0

        rows = [
            dict(name='spending_final',
                 label='Spending on goods and services',
                 value=safe(getattr(p, 'spending_net', None))),
            dict(name='debt_repay_final',
                 label='Debt repayment',
                 value=safe(getattr(p, 'debt_repay_net', None))),
            dict(name='labor_income_final',
                 label='Labor income',
                 value=safe(getattr(p, 'labor_income_net', None))),
            dict(name='new_debt_final',
                 label='New debt',
                 value=safe(getattr(p, 'new_debt_net', None))),
            dict(name='save_invest_final',
                 label='Savings and investments',
                 value=safe(getattr(p, 'save_invest_net', None))),
        ]

        return dict(rows=rows)

    def before_next_page(player):
        part = player.participant

        # Fill missing finals with initial values
        player.spending_final = (
            player.spending_final
            if player.spending_final is not None
            else part.spending_net
        )

        player.debt_repay_final = (
            player.debt_repay_final
            if player.debt_repay_final is not None
            else part.debt_repay_net
        )

        player.labor_income_final = (
            player.labor_income_final
            if player.labor_income_final is not None
            else part.labor_income_net
        )

        player.new_debt_final = (
            player.new_debt_final
            if player.new_debt_final is not None
            else part.new_debt_net
        )

        player.save_invest_final = (
            player.save_invest_final
            if player.save_invest_final is not None
            else part.save_invest_net
        )

        # Detect whether *any* revision occurred
        player.revised_any = any([
            player.spending_final != part.spending_net,
            player.debt_repay_final != part.debt_repay_net,
            player.labor_income_final != part.labor_income_net,
            player.new_debt_final != part.new_debt_net,
            player.save_invest_final != part.save_invest_net,
        ])

    def error_message(player, values):
        part = player.participant

        revised = any([
            values['spending_final'] != part.spending_net,
            values['debt_repay_final'] != part.debt_repay_net,
            values['labor_income_final'] != part.labor_income_net,
            values['new_debt_final'] != part.new_debt_net,
            values['save_invest_final'] != part.save_invest_net,
        ])

        if revised:
            reasons = [
                values['revision_misunderstood'],
                values['revision_rethought_less'],
                values['revision_rethought_more'],
                values['revision_context'],
                values['revision_mistake'],
                values['revision_other'],
            ]

            if not any(reasons):
                return (
                    "You changed at least one answer. "
                    "Please indicate why you revised your response."
                )

            if values['revision_other'] and not values['revision_other_text']:
                return "Please specify the reason for your revision."

class elicitationT1(Page):
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
        return  player.subsession.Treatment == 2 or player.subsession.Treatment == 3 and player.participant.received_stimulus ==2

    def before_next_page(player, timeout_happened):
        debt(player)

class ElicitationT1(Page):
    form_model = 'player'
    form_fields = [
        # Spending
        'spend_increase', 'spend_same_or_decrease', 'spend_amount',
        'spend_everyday', 'spend_leisure', 'spend_services', 'spend_durable',

        # Debt repayment
        'debt_increase', 'debt_same_or_decrease', 'debt_amount',
        'debt_cc', 'debt_bills', 'debt_short', 'debt_long',

        # Labor
        'labor_decrease', 'labor_same_or_increase',
        'labor_hours', 'labor_income',
        'labor_gigs', 'labor_overtime', 'labor_holidays', 'labor_contract',

        # New debt
        'newdebt_increase', 'newdebt_amount','newdebt_same_or_decrease',
        'newdebt_cc', 'newdebt_bills', 'newdebt_short', 'newdebt_long',

        # Savings
        'save_increase', 'save_same_or_decrease', 'save_amount',
        'save_accounts', 'save_lowrisk', 'save_risky',
        'save_realestate', 'save_business', 'save_crypto',
    ]

def error_message(self, values):
    def check(total, components):
        if not total:
            return True
        alloc_sum = sum(v or 0 for v in components)
        return abs(alloc_sum - total) < 1

    checks = [
        check(values['spend_amount'], [
            values['spend_everyday'], values['spend_leisure'],
            values['spend_services'], values['spend_durable']
        ]),
        check(values['debt_amount'], [
            values['debt_cc'], values['debt_bills'],
            values['debt_short'], values['debt_long']
        ]),
        check(values['newdebt_amount'], [
            values['newdebt_cc'], values['newdebt_bills'],
            values['newdebt_short'], values['newdebt_long']
        ]),
        check(values['save_amount'], [
            values['save_accounts'], values['save_lowrisk'],
            values['save_risky'], values['save_realestate'],
            values['save_business'], values['save_crypto']
        ]),
    ]

    if not all(checks):
        return (
            "Some allocations do not add up to the total amounts you entered. "
            "Please correct them before continuing."
        )


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
        return  player.subsession.Treatment == 3 and player.participant.received_stimulus ==1

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
        return player.subsession.Treatment == 1 and player.participant.debt_repay!=0 or player.subsession.Treatment == 2 and player.participant.debt_repay!=0 or player.subsession.Treatment==3 and player.participant.received_stimulus ==2 and player.participant.debt_repay!=0

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
        return player.subsession.Treatment==3 and player.participant.received_stimulus ==1 and player.participant.debt_repay!=0






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
        return player.subsession.Treatment == 2 and player.participant.debt_new!=0 or player.subsession.Treatment==3 and player.participant.received_stimulus ==2 and player.participant.debt_new!=0

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
        return  player.subsession.Treatment==3 and player.participant.received_stimulus ==1  and player.participant.debt_new!=0


class FeedbackElicitation(Page):
    form_model = 'player'
    form_fields = [
        'understanding_difficulty',
        'mental_effort',
        'categories_cover',
        'attention2',
        'categories_specify',
    ]

    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.Treatment == 1 or player.subsession.Treatment == 2 or player.subsession.Treatment == 3 and player.participant.received_stimulus == 2


class FeedbackElicitationT2(Page):
    form_model = 'player'
    form_fields = [
        'understanding_difficulty',
        'mental_effort',
        'categories_cover',
        'attention2',
        'categories_specify',
    ]

    @staticmethod
    def is_displayed(player: Player):
        return  player.subsession.Treatment == 3 and player.participant.received_stimulus==1

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
        return player.subsession.Treatment == 1 or player.subsession.Treatment == 2 or player.subsession.Treatment == 3 and player.participant.received_stimulus==2
class PaymentInterpretationT2(Page):
    form_model = 'player'
    form_fields = [
        'deposit_account',
        'payment_different_if_personal',
        'payment_different_explain',
    ]

    def error_message(self, values):
        dep = values.get('deposit_account')
        diff = values.get('payment_different_if_personal')
        explain = values.get('payment_different_explain')

        # Q2 required only if deposit_account ∈ {2,3,4}
        if dep in [2, 3, 4]:
            if diff is None:
                return 'Please answer Question 2.'

            # Explanation required only if Q2 = Yes (assuming Yes = 1)
            if diff == 1 and not explain:
                return 'Please explain your answer to Question 2.'

    @staticmethod
    def is_displayed(player: Player):
        return (
            player.subsession.Treatment == 3
            and player.participant.received_stimulus == 1
        )

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

    def before_next_page(player, timeout_happened):
        correct_Robin(player)

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

    def before_next_page(player, timeout_happened):
        correct_RobinT0(player)

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

    def before_next_page(player, timeout_happened):
        correct_TaylorT0(player)



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

    def before_next_page(player, timeout_happened):
        correct_Taylor(player)


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

    def before_next_page(player, timeout_happened):
        correct_Charlie(player)
        set_payoff(player)
        set_payoff_questions(player)

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

    def before_next_page(player, timeout_happened):
        correct_CharlieT0(player)
        set_payoff(player)
        set_payoff_questions(player)



class FeedbackScenario(Page):
    form_model = 'player'
    form_fields = [
        'categories_cover_scenario',
        'categories_specify_scenario',
    ]


class End(Page):
    form_model = 'player'

class ProlificBack(Page):
    form_model = 'player'
    @staticmethod
    def js_vars(player):
        return dict(
            completionlink=
            player.subsession.session.config['completionlink']
        )
#page_sequence = [InstructionsPart2,InstructionsPart2T2, instructionsT0, instructionsT1, ElicitationT1, instructionsT2, ElicitationT0,Spending,DebtRepayment, Labor,NewDebt,SavingsInvestments,  ElicitationT2, FeedbackElicitation , FeedbackElicitationT2,PaymentInterpretation,PaymentInterpretationT2, InstructionsScenarios, Robin, RobinT0, Taylor, TaylorT0, Charlie, CharlieT0, FeedbackScenario,End,ProlificBack]
#

page_sequence = [InstructionsPart2,InstructionsPart2T2, instructionsT0, instructionsT1, ElicitationT1, instructionsT2, ElicitationT0, ElicitationT2, FeedbackElicitation , FeedbackElicitationT2,PaymentInterpretation,PaymentInterpretationT2, InstructionsScenarios, Robin, RobinT0, Taylor, TaylorT0, Charlie, CharlieT0, FeedbackScenario,End,ProlificBack]
#
#page_sequence = [InstructionsPart2,InstructionsPart2T2, instructionsT0, instructionsT1,  instructionsT2, ElicitationT0,ElicitationT1, ElicitationT2, FeedbackElicitation , FeedbackElicitationT2,QuestionsDebtRepay,QuestionsDebtRepayT2, QuestionsDebtNew, QuestionsDebtNewT2,PaymentInterpretation,PaymentInterpretationT2, InstructionsScenarios, Robin, RobinT0, Taylor, TaylorT0, Charlie, CharlieT0, FeedbackScenario,End,ProlificBack]

#page_sequence =[Robin, RobinT0, Taylor, TaylorT0, Charlie, CharlieT0, FeedbackScenario,End,ProlificBack]