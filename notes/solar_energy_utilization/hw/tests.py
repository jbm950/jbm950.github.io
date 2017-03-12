import numpy as np
import unittest
import datetime
import funcs
import hw5


class TestIsNear(unittest.TestCase):
    def test_is_near(self):
        assert funcs.is_near(5, 2, 1) == False
        assert funcs.is_near(1.5, 2, 1) == True
        assert funcs.is_near(2.5, 2, 1) == True


class TestHourAngle(unittest.TestCase):
    def test_hour_angle_values(self):
        time1 = datetime.time(8, 0, 0)
        time2 = datetime.time(16, 0, 0)
        time3 = datetime.time(8, 33, 0)

        omega_expected_1 = -60
        omega_expected_2 = 60
        omega_expected_3 = -51.75

        omega1 = funcs.hour_angle(time1)
        omega2 = funcs.hour_angle(time2)
        omega3 = funcs.hour_angle(time3)

        assert omega1 - omega_expected_1 == 0
        assert omega2 - omega_expected_2 == 0
        assert omega3 - omega_expected_3 == 0


class TestIncidenceAngle(unittest.TestCase):
    def test_incidence_angle_values(self):
        pass


class TestSolarAzimuthAngle(unittest.TestCase):
    def test_solar_azimuth_angle_values(self):
        omega = 7.35
        thetaz = 9.03
        phi = 29.65
        delta = 23.45

        gamma_s_expected = 48.38
        tol = 0.02

        gamma_s = funcs.solar_azimuth_angle(omega, thetaz, phi, delta)

        assert funcs.is_near(gamma_s, gamma_s_expected, tol)


class TestSolarTime(unittest.TestCase):
    def test_solar_time_values(self):
        pass


class TestZenithAngle(unittest.TestCase):
    def test_zenith_angle_values(self):
        phi = 29.65
        delta = 23.45
        omega = 7.35

        thetaz_expected = 9.03
        tol = 0.005

        thetaz = funcs.zenith_angle(phi, delta, omega)

        assert funcs.is_near(thetaz, thetaz_expected, tol)

# Tests for ray tracing code
class TestRayTraceing(unittest.TestCase):
    theta = 5
    f = 2
    # Points to test x1 = -2.5 and x1 = 1.5
    def test_oneD_parabola(self):
        # Create expected values
        y1a_expect = 0.78125
        y1b_expect = 0.28125

        # Calculated the values
        y1a = hw5.oneD_parabola(-2.5, self.f)
        y1b = hw5.oneD_parabola(1.5, self.f)

        assert y1a - y1a_expect == 0
        assert y1b - y1b_expect == 0

    def test_step2(self):
        # Create expected values
        x2a_expect = -2.41284
        x2b_expect = 1.587155

        y2a_expect = 1.777444
        y2b_expect = 1.277444

        # Calculate the values
        theta = np.radians(self.theta)
        x2a, y2a = hw5.step2(-2.5, 0.78125, theta)
        x2b, y2b = hw5.step2(1.5, 0.28125, theta)
        tol = 0.00001

        assert funcs.is_near(x2a_expect, x2a, tol)
        assert funcs.is_near(x2b_expect, x2b, tol)
        assert funcs.is_near(y2a_expect, y2a, tol)
        assert funcs.is_near(y2b_expect, y2b, tol)

    def test_step3_twoD(self):
        # Create expected values
        x3a_expect = -1.652
        x3b_expect = 2.436329

        y3a_expect = 0.251254
        y3b_expect = 0.632374

        # Calculate the values
        x3a, y3a = hw5.step3_twoD(-2.5, 0.78125, 2)
        x3b, y3b = hw5.step3_twoD(1.5, 0.28125, 2)
        tol = 0.001

        assert funcs.is_near(x3a_expect, x3a, tol)
        assert funcs.is_near(x3b_expect, x3b, tol)
        assert funcs.is_near(y3a_expect, y3a, tol)
        assert funcs.is_near(y3b_expect, y3b, tol)

        # Test that the line is tangent
        assert funcs.is_near((y3a-0.78125)/(x3a+2.5), (-2.5)/(2*self.f), tol)
        assert funcs.is_near((y3b-0.28125)/(x3b-1.5), (1.5)/(2*self.f), tol)

    def test_step4(self):
        # Create expected values
        x4a_expect = -1.97
        x4b_expect = 1.148876

        y4a_expect = 1.62924
        y4b_expect = 1.21758

        # Calculate the values
        x4a, y4a = hw5.step4(-2.5, 0.78125, -1.652, 0.251254)
        x4b, y4b = hw5.step4(1.5, 0.28125, 2.436329, 0.632374)
        tol = 0.0001

        assert funcs.is_near(x4a_expect, x4a, tol)
        assert funcs.is_near(x4b_expect, x4b, tol)
        assert funcs.is_near(y4a_expect, y4a, tol)
        assert funcs.is_near(y4b_expect, y4b, tol)

        # Test that it is normal to the tangent vector
        dota = ((-1.652 + 2.5)*(-1.97 + 2.5) +
                (0.251254 - 0.78125)*(1.62924 - 0.78125))
        dotb = ((2.436329-1.5)*(1.148876-1.5) +
                (0.632374 - 0.28125)*(1.21758 - 0.28125))

        assert funcs.is_near(dota, 0, tol)
        assert funcs.is_near(dotb, 0, tol)

    def test_step5(self):
        # Create the expected values
        x5a_expect = -1.6427456
        x5b_expect = 0.7793

        y5a_expect = 1.2961
        y5b_expect = 0.9745

        # Calculate the values
        x5a, y5a = hw5.step5(-2.5, 0.78125, -2.41284, 1.777444, -1.97, 1.62924)
        x5b, y5b = hw5.step5(1.5, 0.28125, 1.587155, 1.277444, 1.148876, 1.21758)
        tol = 0.001

        assert funcs.is_near(x5a_expect, x5a, tol)
        assert funcs.is_near(x5b_expect, x5b, tol)
        assert funcs.is_near(y5a_expect, y5a, tol)
        assert funcs.is_near(y5b_expect, y5b, tol)

    def test_plane_intercept(self):
        # Create the expected values
        xa_expect = -0.4707122
        xb_expect = -0.28681

        # Calculate the values
        xa = hw5.plane_intercept(-2.5, 0.78125, -1.6427456, 1.2961, 2)
        xb = hw5.plane_intercept(1.5, 0.28125, 0.7793, 0.9745, 2)
        tol = 0.001

        assert funcs.is_near(xa_expect, xa, tol)
        assert funcs.is_near(xb_expect, xb, tol)

if __name__ == "__main__":
    unittest.main()
