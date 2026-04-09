import pandas as pd
from collections import defaultdict

def load_and_aggregate_data(filepath):
    df = pd.read_excel(filepath)

    group_cols = [
        'year', 'plant_id', 'produced_material',
        'produced_material_production_type', 'produced_material_release_type',
        'component_material', 'component_material_production_type',
        'component_material_release_type'
    ]

    return df.groupby(group_cols, dropna=False).agg({
        'produced_material_quantity': 'sum',
        'component_material_quantity': 'sum'
    }).reset_index()


def build_bom_graph(df_group) -> dict:
    adj_list = defaultdict(list)
    for row in df_group.itertuples(index=False):
        key = (row.plant_id, row.year, row.produced_material)
        adj_list[key].append(row)
    return adj_list

def get_unique_fin_materials(df_group) -> list:
    fin_df = df_group[df_group['produced_material_release_type'] == 'FIN']
    cols = [
        'year',
        'plant_id', 'produced_material',
        'produced_material_production_type',
        'produced_material_release_type',
        'produced_material_quantity'
    ]
    return list(fin_df.loc[:, cols].drop_duplicates().itertuples(index=False))

def explode_generator(unique_fin_list, adj_list):
    for fin in unique_fin_list:
        queue = [fin.produced_material]
        while queue:
            cur_material = queue.pop(0)
            components = adj_list.get((fin.plant_id, fin.year, cur_material), [])
            for comp in components:
                yield {
                    'plant': fin.plant_id,
                    'fin_material_id': fin.produced_material,
                    'fin_material_release_type': fin.produced_material_release_type,
                    'fin_material_production_type': fin.produced_material_production_type,
                    'fin_production_quantity': fin.produced_material_quantity,

                    'prod_material_id': comp.produced_material,
                    'prod_material_release_type': comp.produced_material_release_type,
                    'prod_material_production_type': comp.produced_material_production_type,
                    'prod_material_production_quantity': comp.produced_material_quantity,

                    'component_id': comp.component_material,
                    'component_material_release_type': comp.component_material_release_type,
                    'component_material_production_type': comp.component_material_production_type,
                    'component_consumption_quantity': comp.component_material_quantity,
                    'year': fin.year
                }

                if comp.component_material_release_type == 'PROD':
                    queue.append(comp.component_material)

def final_output(generator):
    final_df = pd.DataFrame(generator)
    cols_to_int = [
        'fin_material_production_type',
        'prod_material_production_type',
        'component_material_production_type'
    ]
    for col in cols_to_int:
        if col in final_df.columns:
            final_df[col] = final_df[col].astype('Int64')

    final_df.columns = [col.lower() for col in final_df.columns]
    return final_df

def main():
    filepath = "task_2_data_ex.xlsx"
    df_group = load_and_aggregate_data(filepath)
    adj_list = build_bom_graph(df_group)
    unique_fin = get_unique_fin_materials(df_group)

    bom_generator = explode_generator(unique_fin, adj_list)
    final_df = final_output(bom_generator)
    final_df.to_excel("final.xlsx", index=False)

if __name__ == "__main__":
    main()