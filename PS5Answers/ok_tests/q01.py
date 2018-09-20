test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(KoverY_50_splus, 4.20, atol=0.1) and np.isclose(KoverY_50_gplus, 3.33, atol=0.1) and np.isclose(KoverY_50_nplus, 3.33, atol=0.1)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
