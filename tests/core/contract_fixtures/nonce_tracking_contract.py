# Contract that keeps track of its nonce
nonce_tracking_lll_code = ['seq',
                            ['return',  # noqa: E127
                                0,
                                ['lll',
                                    ['seq',
                                        ['assert', ['eq', ['calldataload', 32], ['sload', 0]]],
                                        ['paygas', ['calldataload', 64]],
                                        ['sstore', 0, ['add', ['sload', 0], 1]],
                                        'stop'],
                                0]]]  # noqa: E128


# Contract that does not keeps track of its nonce
no_nonce_tracking_lll_code = ['seq',
                                ['return',  # noqa: E127
                                    0,
                                    ['lll',
                                        ['seq',
                                            ['paygas', ['calldataload', 64]],
                                            ['sstore', 0, ['add', ['sload', 0], 1]],
                                            'stop'],
                                    0]]]  # noqa: E128
