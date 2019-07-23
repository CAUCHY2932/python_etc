
@api.route('/top_n_city_manager/<uid>')
def top_n_city_manager(uid):
    list_sub_user_id = determine_sub_user_new(uid)
    all = DisplayApplyView.query. \
        filter(and_(DisplayApplyView.start_time.isnot(None),
                    DisplayApplyView.sales_man_code.in_(list_sub_user_id))).all()

    user_list = [(x.sales_man_name, x.sales_man_code) for x in all]

    from collections import Counter
    wc = Counter(user_list)

    result = [{'name': n[0], 'code': n[1], 'count': c, }
              for n, c in wc.most_common(20)]

    return jsonify({
        'code': 200,
        'msg': 'success! the uid is {}'.format(uid),
        'error_code': 0,
        'data': {
            's': result
        }
    })


@api.route('/top_n_salesman/<uid>')
def top_n_salesman(uid):
    list_sub_user_id = determine_sub_user_new(uid)
    all = DisplayApplyView.query. \
        filter(and_(DisplayApplyView.start_time.isnot(None),
                    DisplayApplyView.sales_man_code.in_(list_sub_user_id))).all()

    user_list = [(x.sales_man_name, x.sales_man_code) for x in all]

    from collections import Counter
    wc = Counter(user_list)

    result = [{'order': i+1, 'name': w[0][0], 'code': w[0][1], 'count': w[1], }
              for i, w in enumerate(wc.most_common(20))]

    # result = [{'name': n[0], 'code': n[1], 'count': c, }
    #           for n, c in wc.most_common(20)]

    return jsonify({
        'code': 200,
        'msg': 'success! the uid is {}'.format(uid),
        'error_code': 0,
        'data': {
            'salesman': result
        }
    })


@api.route('/v1/<uid>')
def top_test(uid):
    list_sub_user_id = determine_sub_user_new(uid)
    s = "', '".join(list_sub_user_id)
    # return jsonify({
    #     "s": ', '.join(list_sub_user_id)
    # })
    statement = """
    SELECT
	city_manager_code,
	city_manager_name,
	sum( CASE WHEN apply_times IS NULL THEN 0 ELSE 1 END ) applied,
	sum( CASE WHEN apply_times IS NULL THEN 1 ELSE 0 END ) unapplied ,
	(sum( CASE WHEN apply_times IS NULL THEN 0 ELSE 1 END )+ sum( CASE WHEN apply_times IS NULL THEN 1 ELSE 0 END )) total
    FROM
        display_apply_view v
    WHERE v.sales_man_code in ('%s')
    GROUP BY
        city_manager_code,
        city_manager_name
    ORDER BY applied
    limit 20
    OFFSET 0
    """

    rs = db.session.execute(statement % s)
    return jsonify({
        'data': [{'a': x.city_manager_code,
                  'b': x.city_manager_name,
                  'c': float(x.applied),
                  'd': float(x.unapplied),
                  'e': float(x.total),
                  }
                 for x in rs]
    })



@api.route('/top_n_salesman/<uid>')
def top_n_salesman(uid):
    list_sub_user_id = determine_sub_user_new(uid)
    all = DisplayApplyView.query. \
        filter(and_(DisplayApplyView.start_time.isnot(None),
                    DisplayApplyView.sales_man_code.in_(list_sub_user_id))).all()

    user_list = [(x.sales_man_name, x.sales_man_code) for x in all]

    from collections import Counter
    wc = Counter(user_list)

    result = [{'order': i+1, 'name': w[0][0], 'code': w[0][1], 'count': w[1], }
              for i, w in enumerate(wc.most_common(20))]

    # result = [{'name': n[0], 'code': n[1], 'count': c, }
    #           for n, c in wc.most_common(20)]

    return jsonify({
        'code': 200,
        'msg': 'success! the uid is {}'.format(uid),
        'error_code': 0,
        'data': {
            'salesman': result
        }
    })




@api.route('/top_n_city_manager/<uid>')
def top_n_city_manager(uid):
    list_sub_user_id = determine_sub_user_new(uid)
    all = DisplayApplyView.query. \
        filter(and_(DisplayApplyView.start_time.isnot(None),
                    DisplayApplyView.sales_man_code.in_(list_sub_user_id))).all()

    user_list = [(x.sales_man_name, x.sales_man_code) for x in all]

    from collections import Counter
    wc = Counter(user_list)

    result = [{'name': n[0], 'code': n[1], 'count': c, }
              for n, c in wc.most_common(20)]

    return jsonify({
        'code': 200,
        'msg': 'success! the uid is {}'.format(uid),
        'error_code': 0,
        'data': {
            's': result
        }
    })