from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Coupon

class CouponApplyTest(TestCase):

    def setUp(self):
        self.coupon = Coupon.objects.create(
            code='TESTCODE',
            valid_form=timezone.now(),
            valid_to=timezone.now() + timezone.timedelta(days=7),
            discount=10,
            active=True
        )

    def test_coupon_applied_successfully(self):
        url = reverse('coupons:apply')
        data = {'code': 'TESTCODE'}
        response = self.client.post(url, data, follow=True)
        self.assertRedirects(response, reverse('cart:cart_detail'))
        self.assertEqual(self.client.session['coupon_id'], self.coupon.id)

    def test_coupon_not_found(self):
        url = reverse('coupons:apply')
        data = {'code': 'INVALIDCODE'}
        response = self.client.post(url, data, follow=True)
        self.assertRedirects(response, reverse('cart:cart_detail'))
        self.assertIsNone(self.client.session.get('coupon_id'))