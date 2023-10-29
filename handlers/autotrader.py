from utils import format_string


class AutotraderHandler:

    def name(self, section):
        return format_string(
            section.select_one(
                '.re-layout-wrapper'
            ).find(
                'a', class_='inner-link'
            ).select_one(
                '.re-layout-inner'
            ).select_one(
                '.detail-center-area'
            ).find('span', class_='title-with-trim').text
        )

    def kms(self, section):
        kms = section.select_one('.kms')
        kms_value = None

        if kms:
            kms_value = kms.select_one(
                '.odometer-proximity'
            ).text
        return kms_value

    def price(self, section):
        return section.select_one(
            '.detail-price-area'
        ).select_one(
            '.price'
        ).find('span', class_='price-amount').text

    def image(self, section):
        return section.find(
            'img', class_='photo-image'
        ).get('data-original')

    def region(self, section):
        return section.find(
            'span', class_='proximity-text'
        ).text
