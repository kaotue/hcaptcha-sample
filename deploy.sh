sam build
sam deploy \
--stack-name hcaptcha-sample \
--s3-bucket hcaptcha-sample \
--capabilities CAPABILITY_NAMED_IAM \
--parameter-overrides HCaptchaSiteKey=$HCAPTCHA_SITE_KEY HCaptchaSecret=$HCAPTCHA_SECRET
