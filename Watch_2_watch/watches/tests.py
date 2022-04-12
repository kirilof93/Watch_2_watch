# from django.test import TestCase
# from Watch_2_watch.watches.models import Watch
#
#
# class WatchTesCase(TestCase):
#     def test_yearValidator_when_year_is_correct_shouldDoNothing(self):
#         p = Watch(
#             type='sport',
#             brand='Rolex',
#             production_year=2020,
#             description='',
#             image='',
#             for_sale_status=True,
#             user='evgeni'
#         )
#
#         p.full_clean()
#         p.save()
#
#         self.assertIsNotNone(p)