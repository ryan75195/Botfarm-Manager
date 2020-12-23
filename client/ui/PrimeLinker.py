import time

from selenium import webdriver
import requests as r
import selenium.webdriver.support.ui as ui
class PrimeLinker:

    def __init__(self,primeEmail,primePassword,osrsEmail,osrsPassword):
        self.primeEmail = primeEmail
        self.primePassword = primePassword
        self.osrsEmail = osrsEmail
        self.osrsPassword = osrsPassword
        self.driver = webdriver.Firefox()
        self.amazonLoginPage = "https://www.amazon.com/ap/signin?openid.return_to=https%3A%2F%2Fgaming.amazon.com%2F&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2" \
                               "F2.0%2Fidentifier_select&openid.assoc_handle=amzn_respawn_desktop_us&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%" \
                               "2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&ssoResponse=eyJ6aXAiOiJERUYiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIj" \
                               "oiQTI1NktXIn0._hiZAbTNyS9Irxj_Zai9XgHJAPLV4kxabPaEaWr_-WlOAPDHyYt22A.s-gUiOS6yeZPPdDi.nfD4HDzTJ3EZGGGz7wYhrqDGS76dbAfqEMKOti9jnGWo7Gab2ihm0XoTP1q" \
                               "p0kalIpcwpa7QW4vTgg9JFpSXw8JzZWaP7UOFiTE7hs_e3WSOF3ecSg22IpdyCsyakB5b7HkPkZeWTUqqamaFAHxAeuvP67-gyMVCc8HDqG4c-hYak4vpaiEoRJskf5n1Vo8-C3GhzKkii24gBi-" \
                               "HaW8kEVR536zm7yn-nvlYVareLo71PLNAzYd0N0JY43DH_S0p09VDFBpfZsbCO6y7RFd2BMas2ml0rqm0dINQInf9cw.GiM2_G-_ajujhNEih-txjg"

        self.mailLogin = 'https://account.mail.ru/login?page=https%3A%2F%2Faccount.mail.ru%2F%3F&'
        self.primeRSPage = "https://gaming.amazon.com/loot/runescape?ingress=amzn&ref_=SM_RS06_P1_CRWN?"
        self.driver.implicitly_wait(2)
    def amazon_login(self):
        self.driver.get(self.amazonLoginPage)
        self.driver.find_element_by_id("ap_email").send_keys(self.primeEmail)
        self.driver.find_element_by_id("ap_password").send_keys(self.primePassword)
        self.driver.find_element_by_id("signInSubmit").click()
        if self.doesIDElementExist("auth-captcha-guess"):
            print("Please solve the captcha below.")
            self.driver.find_element_by_id("ap_password").send_keys(self.primePassword)
            self.conditionalSleep(60, "ID", "auth-captcha-guess", False)
        if self.doesIDElementExist("ap_email"):
            print("Login Successful")
    def verifyLogin(self):
        self.driver.get(self.mailLogin)
        self.driver.find_element_by_name("username").send_keys(self.primeEmail)
        self.driver.find_element_by_css_selector("html body div#login-content div#root div div.login-panel div.c019.c0114.c0130.c0112 div.c0113 div form div div div.login-row.last div.c0153.c0154 div button.c01208.c0194.c01220.c01105.c01232.c01118 span.c01212.c0197.c01210.c0195").click()
        self.sleep(3)
        self.driver.find_element_by_name("password").send_keys(self.primePassword)
        self.driver.find_element_by_css_selector("html body div#login-content div#root div div.login-panel div.c019.c0114.c0130.c0112 div.c0113 div form div div div.login-row.last div.c0153.c0154 div div button.c01292.c0194.c01304.c01105.c01316.c01118 span.c01296.c0197.c01294.c0195").click()
        self.sleep(6)
        if self.doesCSSElementExist("html.pm-requestanimationframe.pm-raf.pm-backgroundsize.pm-boxshadow.pm-csstransitions.pm-transitionend.pm-dpr.pm-no-retina.pm-no-ie body div#app div.b-panel.b-panel_responsive.b-panel_service.b-panel_header-responsive-margin-bottom"
                                                                          " div.b-panel__wrapper form.js-form div.b-panel__content div.b-captcha.b-captcha_responsive.b-captcha_block div.b-captcha__code"
                                                                          " input.b-input.b-input_captcha.b-input_responsive.js-captcha"):
            self.conditionalSleep(30, "CSS", "html.pm-requestanimationframe.pm-raf.pm-backgroundsize.pm-boxshadow.pm-csstransitions.pm-transitionend.pm-dpr.pm-no-retina.pm-no-ie body div#app div.b-panel.b-panel_responsive.b-panel_service.b-panel_header-responsive-margin-bottom"
                                                                          " div.b-panel__wrapper form.js-form div.b-panel__content div.b-captcha.b-captcha_responsive.b-captcha_block div.b-captcha__code"
                                                                          " input.b-input.b-input_captcha.b-input_responsive.js-captcha", False)
        if self.doesCSSElementExist("html.a-ws.a-js.a-audio.a-video.a-canvas.a-svg.a-drag-drop.a-geolocation.a-history.a-webworker.a-autofocus.a-input-placeholder.a-textarea-placeholder.a-local-storage.a-gradients.a-transform3d.a-touch-scrolling.a-text-shadow.a-text-stroke.a-box-shadow.a-border-radius.a-border-image.a-opacity.a-transform.a-transition.null body.ap-locale-en_US.a-m-us.a-aui_157141-c.a-aui_158613-c.a-aui_72554-c.a-aui_dropdown_187959-c.a-aui_pci_risk_banner_210084-c.a-aui_perf_130093-c.a-aui_tnr_v2_180836-c.a-aui_ux_145937-c.a-meter-animate div#a-page div.a-section.a-padding-medium.auth-workflow div#authportal-center-section.a-section div#authportal-main-section.a-section div.a-section.a-spacing-base.auth-pagelet-container div.a-section div#auth-warning-message-box.a-box.a-alert.a-alert-warning.auth-server-side-message-box.a-spacing-base div.a-box-inner.a-alert-container h4.a-alert-heading"):
            self.driver.find_element_by_name("password").send_keys(self.primePassword)
            self.conditionalSleep(30, "Text", "To continue, approve the notification sent to", True)

        self.driver.find_element_by_css_selector("html body.page.g-default-font.theme-default div#app-canvas div.application div.application-mail div.application-mail__overlay div.application-mail__wrap div.layout.layout_size_m.layout_type_2pane.layout_left-size_58.layout_right-size_60.layout_bordered div.layout__main-frame div div.layout__sidebar.layout__sidebar_size-80 div.letter-list.letter-list_has-letters div.scrollable.g-scrollable.scrollable_bright.scrollable_footer div.scrollable__container div.dataset-letters div.draggable div.dataset.dataset_select-mode_off div.dataset__items a.llc.js-tooltip-direction_letter-bottom.js-letter-list-item.llc_normal div.llc__container div.llc__content").click()
        self.sleep(2)
        link = self.driver.find_element_by_xpath("//*[contains(text(), 'https://www.amazon.com/')]").text
        self.driver.get(link)
        self.sleep(10)
        # if self.doesCSSElementExist("Thank you. Sign-in attempt was approved."):
        #     return 0
        if self.doesNameElementExist("customerResponseApproveButton"):
            self.driver.find_element_by_name("customerResponseApproveButton").click()
            self.sleep(2)


        # self.driver.find_element_by_css_selector("#customSelect_3 span.selectLabel").click()
        # self.driver.findElement(By.cssSelector("#customSelect_3 span.selectLabel"))
        # .getAttribute("innerHTML");

    def linkRunescape(self):
        # open osrs prime page
        self.driver.get(self.primeRSPage)
        self.sleep(2)
        # click box
        self.driver.find_element_by_css_selector("html body div#root div.prime-root-minimal.tw-c-background-base.tw-flex.tw-flex-column.tw-full-height.tw-relative.tw-root--hover.tw-root--theme-dark main.tw-c-background-alt.tw-flex-grow-1.tw-full-height.tw-full-width.tw-relative div.tw-flex.tw-flex-column.tw-full-height.tw-full-width div.prime-main.tw-c-background-base.tw-flex-grow-1 div.tw-c-background-base.tw-flex-grow-2 div.loot-cards-container.tw-lg-mg-l-10.tw-mg-b-3.tw-mg-x-3.tw-relative.tw-sm-mg-r-0.tw-z-above div.loot-cards.tw-align-center.tw-flex.tw-flex-wrap.tw-full-width.tw-justify-content-center.tw-sm-inline-block div.loot-card__container.tw-align-bottom.tw-inline-block.tw-relative div.loot-card.tw-border-radius-medium.tw-c-text-prime.tw-flex.tw-flex-column.tw-flex-nowrap.tw-mg-05.tw-relative div.tw-flex.tw-flex-column.tw-flex-nowrap.tw-overflow-hidden.tw-relative button.tw-interactive.loot-card__image__container img.loot-card__image.loot-card__image__clickable.tw-image").click()
        self.sleep(2)

        # click claim now
        self.driver.find_element_by_css_selector("html body.ReactModal__Body--open div.ReactModalPortal div.ReactModal__Overlay.ReactModal__Overlay--after-open.modal__backdrop.modal__backdrop--standard div.ReactModal__Content.ReactModal__Content--after-open.modal__content.modal__content--standard.tw-root--theme-dark.tw-root--hover div.loot-details-modal.tw-align-content-start.tw-c-background-accent-alt-2.tw-c-text-base.tw-flex.tw-flex-wrap.tw-sm-flex-nowrap div.loot-details-modal__info div.loot-details-modal__info__cta.tw-align-items-center.tw-c-background-accent-alt.tw-flex.tw-flex-column.tw-full-width.tw-hide.tw-justify-content-center.tw-lg-pd-x-7.tw-sm-flex.tw-sm-pd-x-2 div.call-to-action.tw-align-items-center.tw-c-text-accent-alt-2.tw-flex.tw-flex-grow-0.tw-flex-shrink-1.tw-flex-wrap.tw-full-width.tw-justify-content-center div.call-to-action__container.tw-block.tw-flex-grow-1.tw-full-height button.tw-interactive.tw-border-radius-none.tw-button.tw-button--full-height.tw-button--full-width.tw-button--prime span.tw-button__text div.tw-align-items-center.tw-flex.tw-justify-content-center.tw-pd-1").click()
        self.sleep(2)

        # click link account
        self.driver.find_element_by_css_selector("html body.ReactModal__Body--open div.ReactModalPortal div.ReactModal__Overlay.ReactModal__Overlay--after-open.modal__backdrop.modal__backdrop--standard div.ReactModal__Content.ReactModal__Content--after-open.modal__content.modal__content--standard.tw-root--theme-dark.tw-root--hover div div.account-link-modal.tw-c-background-base.tw-full-height div.tw-align-center.tw-c-background-accent-alt.tw-pd-2.tw-sm-pd-4 a.tw-interactive.tw-button.tw-button--prime span.tw-button__text div.tw-align-items-center.tw-flex.tw-justify-content-center.tw-pd-1").click()
        self.sleep(10)
        if self.doesIDElementExist("imperva_title"):
            print("Captcha")
            self.driver.find_element_by_css_selector("html body#p-error-vista.p-error-vista main.l-vista.l-vista--size-narrow div.l-vista__central div#l-vista__container.l-vista__container div#captcha-box.captcha div.geetest_holder.geetest_wind.geetest_detect div.geetest_btn").click()
            self.conditionalSleep(60, "CSS", "html body#p-error-vista.p-error-vista main.l-vista.l-vista--size-narrow div.l-vista__central"
                                             " div#l-vista__container.l-vista__container div#captcha-box.captcha div.geetest_holder.geetest_wind.geetest_detect"
                                             " div.geetest_btn div.geetest_radar_btn div.geetest_radar_tip span.geetest_radar_tip_content", False)
        print("done")
    def run(self):
        self.amazon_login()
        self.verifyLogin()
        self.linkRunescape()

    def sleep(self ,timeSeconds):
        start = time.time()
        while time.time() - start < timeSeconds:
          pass

    def conditionalSleep(self, timeout, type, arg, visible):
        start = time.time()
        while time.time() - start < timeout:

            if type == "CSS":
                if visible and self.doesCSSElementExist(arg):
                    print("Element appeared")
                    break
                if not visible and not self.doesCSSElementExist(arg):
                    print("Element gone")
                    break
            if type == "Text":
                if visible and self.doesTextElementExist(arg):
                    print("Element appeared")
                    break
                if not visible and not self.doesTextElementExist(arg):
                    print("Element gone")
                    break
            if type == "ID":
                if visible and self.doesIDElementExist(arg):
                    print("Element appeared")
                    break
                if not visible and not self.doesIDElementExist(arg):
                    print("Element gone")
                    break
            if type == "Name":
                if visible and self.doesNameElementExist(arg):
                    print("Element appeared")
                    break
                if not visible and not self.doesNameElementExist(arg):
                    print("Element gone")
                    break

    def doesCSSElementExist(self, elementCSS):
        elementList = self.driver.find_elements_by_css_selector(elementCSS)
        return elementList != []
    def doesTextElementExist(self, elementText):
        elementList = self.driver.find_elements_by_xpath(f"//*[contains(text(), '{elementText}')]")
        return elementList != []
    def doesNameElementExist(self, elementName):
        elementList = self.driver.find_elements_by_name(elementName)
        return elementList != []
    def doesIDElementExist(self, elementID):
        elementList = self.driver.find_elements_by_id(elementID)
        return elementList != []
               # and elementList[0] != None and elementList[0].is_displayed()
