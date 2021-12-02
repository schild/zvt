# -*- coding: utf-8 -*-
from zvt.api.utils import to_report_period_type
from zvt.domain import CashFlowStatement
from zvt.recorders.eastmoney.finance.base_china_stock_finance_recorder import BaseChinaStockFinanceRecorder
from zvt.utils.time_utils import to_pd_timestamp
from zvt.utils.utils import add_func_to_value, first_item_to_float

cash_flow_map = {
    "cash_from_selling": "Salegoodsservicerec",
    "tax_refund": "Taxreturnrec",
    "cash_from_other_op": "Otheroperaterec",
    "total_op_cash_inflows": "Sumoperateflowin",
    "cash_to_goods_services": "Buygoodsservicepay",
    "cash_to_employees": "Employeepay",
    "taxes_and_surcharges": "Taxpay",
    "cash_to_other_related_op": "Otheroperatepay",
    "total_op_cash_outflows": "Sumoperateflowout",
    "net_op_cash_flows": "Netoperatecashflow",
    "cash_from_disposal_of_investments": "Disposalinvrec",
    "cash_from_returns_on_investments": "Invincomerec",
    "cash_from_disposal_fixed_intangible_assets": "Dispfilassetrec",
    "cash_from_disposal_subsidiaries": "Dispsubsidiaryrec",
    "cash_from_other_investing": "Otherinvrec",
    "total_investing_cash_inflows": "Suminvflowin",
    "cash_to_acquire_fixed_intangible_assets": "Buyfilassetpay",
    "cash_to_investments": "Invpay",
    "cash_to_acquire_subsidiaries": "Getsubsidiarypay",
    "cash_to_other_investing": "Otherinvpay",
    "total_investing_cash_outflows": "Suminvflowout",
    "net_investing_cash_flows": "Netinvcashflow",
    "cash_from_accepting_investment": "Acceptinvrec",
    "cash_from_subsidiaries_accepting_minority_interest": "Subsidiaryaccept",
    "cash_from_borrowings": "Loanrec",
    "cash_from_issuing_bonds": "Issuebondrec",
    "cash_from_other_financing": "Otherfinarec",
    "total_financing_cash_inflows": "Sumfinaflowin",
    "cash_to_repay_borrowings": "Repaydebtpay",
    "cash_to_pay_interest_dividend": "Diviprofitorintpay",
    "cash_to_pay_subsidiaries_minority_interest": "Subsidiarypay",
    "cash_to_other_financing": "Otherfinapay",
    "total_financing_cash_outflows": "Sumfinaflowout",
    "net_financing_cash_flows": "Netfinacashflow",
    "foreign_exchange_rate_effect": "Effectexchangerate",
    "net_cash_increase": "Nicashequi",
    "cash_at_beginning": "Cashequibeginning",
    "cash": "Cashequiending",
    "fi_deposit_increase": "Nideposit",
    "fi_borrow_from_central_bank_increase": "Niborrowfromcbank",
    "fi_deposit_in_others_decrease": "Nddepositincbankfi",
    "fi_borrowing_and_sell_repurchase_increase": "Niborrowsellbuyback",
    "fi_sell_repurchase_increase": "Nisellbuybackfasset",
    "fi_lending_and_buy_repurchase_decrease": "Ndlendbuysellback",
    "fi_buy_repurchase_decrease": "Ndbuysellbackfasset",
    "fi_cash_from_interest_commission": "Intandcommrec",
    "fi_loan_advance_increase": "Niloanadvances",
    "fi_deposit_in_others_increase": "Nidepositincbankfi",
    "fi_lending_and_buy_repurchase_increase": "Nilendsellbuyback",
    "fi_lending_increase": "Nilendfund",
    "fi_borrowing_and_sell_repurchase_decrease": "Ndborrowsellbuyback",
    "fi_borrowing_decrease": "Ndborrowfund",
    "fi_sell_repurchase_decrease": "Ndsellbuybackfasset",
    "fi_cash_to_interest_commission": "Intandcommpay",
    "fi_account_receivable_increase": "Niaccountrec",
    "fi_cash_to_pay_interest": "Bondintpay",
    "fi_cash_from_premium_of_original": "Premiumrec",
    "fi_insured_deposit_increase": "Niinsureddepositinv",
    "fi_bank_broker_sell_repurchase_increase": "Nisellbuyback",
    "fi_bank_broker_buy_repurchase_decrease": "Ndbuysellback",
    "fi_cash_to_insurance_claim": "Indemnitypay",
    "fi_cash_to_reinsurance": "Netripay",
    "fi_lending_decrease": "Ndlendfund",
    "fi_bank_broker_sell_repurchase_decrease": "Ndsellbuyback",
    "fi_cash_to_dividends": "Divipay",
    "fi_insured_pledge_loans_increase": "Niinsuredpledgeloan",
    "fi_cash_to_acquire_subsidiaries": "Buysubsidiarypay",
    "fi_cash_to_disposal_subsidiaries": "Dispsubsidiarypay",
    "fi_cash_to_sell_repurchase": "Netsellbuybackfassetpay",
    "fi_borrowing_increase": "Niborrowfund",
    "fi_cash_from_trading_agent": "Agenttradesecurityrec",
    "fi_cash_from_repurchase_increase": "Nibuybackfund",
    "fi_disposal_trade_asset_decrease": "Nddisptradefasset",
    "fi_repurchase_decrease": "Ndbuybackfund",
    "fi_cash_to_agent_trade": "Agenttradesecuritypay",
}


add_func_to_value(cash_flow_map, first_item_to_float)
cash_flow_map["report_period"] = ("ReportDate", to_report_period_type)
cash_flow_map["report_date"] = ("ReportDate", to_pd_timestamp)


class ChinaStockCashFlowRecorder(BaseChinaStockFinanceRecorder):
    data_schema = CashFlowStatement

    url = 'https://emh5.eastmoney.com/api/CaiWuFenXi/GetXianJinLiuLiangBiaoList'
    finance_report_type = 'XianJinLiuLiangBiaoList'
    data_type = 4

    def get_data_map(self):
        return cash_flow_map


if __name__ == '__main__':
    # init_log('cash_flow.log')
    recorder = ChinaStockCashFlowRecorder(codes=['002572'])
    recorder.run()
# the __all__ is generated
__all__ = ['ChinaStockCashFlowRecorder']