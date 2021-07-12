# -*- coding: utf-8 -*-

# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from google.cloud.aiplatform_v1beta1.types import (
    accelerator_type as accelerator_type_v1beta1,
    annotation as annotation_v1beta1,
    annotation_spec as annotation_spec_v1beta1,
    batch_prediction_job as batch_prediction_job_v1beta1,
    completion_stats as completion_stats_v1beta1,
    custom_job as custom_job_v1beta1,
    data_item as data_item_v1beta1,
    data_labeling_job as data_labeling_job_v1beta1,
    dataset as dataset_v1beta1,
    dataset_service as dataset_service_v1beta1,
    deployed_model_ref as deployed_model_ref_v1beta1,
    encryption_spec as encryption_spec_v1beta1,
    endpoint as endpoint_v1beta1,
    endpoint_service as endpoint_service_v1beta1,
    env_var as env_var_v1beta1,
    explanation as explanation_v1beta1,
    explanation_metadata as explanation_metadata_v1beta1,
    hyperparameter_tuning_job as hyperparameter_tuning_job_v1beta1,
    io as io_v1beta1,
    job_service as job_service_v1beta1,
    job_state as job_state_v1beta1,
    machine_resources as machine_resources_v1beta1,
    manual_batch_tuning_parameters as manual_batch_tuning_parameters_v1beta1,
    model as model_v1beta1,
    model_evaluation as model_evaluation_v1beta1,
    model_evaluation_slice as model_evaluation_slice_v1beta1,
    model_service as model_service_v1beta1,
    operation as operation_v1beta1,
    pipeline_job as pipeline_job_v1beta1,
    pipeline_service as pipeline_service_v1beta1,
    pipeline_state as pipeline_state_v1beta1,
    prediction_service as prediction_service_v1beta1,
    specialist_pool as specialist_pool_v1beta1,
    specialist_pool_service as specialist_pool_service_v1beta1,
    study as study_v1beta1,
    training_pipeline as training_pipeline_v1beta1,
    metadata_service as metadata_service_v1beta1,
    tensorboard as tensorboard_v1beta1,
    tensorboard_data as tensorboard_data_v1beta1,
    tensorboard_experiment as tensorboard_experiment_v1beta1,
    tensorboard_run as tensorboard_run_v1beta1,
    tensorboard_service as tensorboard_service_v1beta1,
    tensorboard_time_series as tensorboard_time_series_v1beta1,
)
from google.cloud.aiplatform_v1.types import (
    accelerator_type as accelerator_type_v1,
    annotation as annotation_v1,
    annotation_spec as annotation_spec_v1,
    batch_prediction_job as batch_prediction_job_v1,
    completion_stats as completion_stats_v1,
    custom_job as custom_job_v1,
    data_item as data_item_v1,
    data_labeling_job as data_labeling_job_v1,
    dataset as dataset_v1,
    dataset_service as dataset_service_v1,
    deployed_model_ref as deployed_model_ref_v1,
    encryption_spec as encryption_spec_v1,
    endpoint as endpoint_v1,
    endpoint_service as endpoint_service_v1,
    env_var as env_var_v1,
    hyperparameter_tuning_job as hyperparameter_tuning_job_v1,
    io as io_v1,
    job_service as job_service_v1,
    job_state as job_state_v1,
    machine_resources as machine_resources_v1,
    manual_batch_tuning_parameters as manual_batch_tuning_parameters_v1,
    model as model_v1,
    model_evaluation as model_evaluation_v1,
    model_evaluation_slice as model_evaluation_slice_v1,
    model_service as model_service_v1,
    operation as operation_v1,
    pipeline_service as pipeline_service_v1,
    pipeline_state as pipeline_state_v1,
    prediction_service as prediction_service_v1,
    specialist_pool as specialist_pool_v1,
    specialist_pool_service as specialist_pool_service_v1,
    study as study_v1,
    training_pipeline as training_pipeline_v1,
)

__all__ = (
    # v1
    accelerator_type_v1,
    annotation_v1,
    annotation_spec_v1,
    batch_prediction_job_v1,
    completion_stats_v1,
    custom_job_v1,
    data_item_v1,
    data_labeling_job_v1,
    dataset_v1,
    dataset_service_v1,
    deployed_model_ref_v1,
    encryption_spec_v1,
    endpoint_v1,
    endpoint_service_v1,
    env_var_v1,
    hyperparameter_tuning_job_v1,
    io_v1,
    job_service_v1,
    job_state_v1,
    machine_resources_v1,
    manual_batch_tuning_parameters_v1,
    model_v1,
    model_evaluation_v1,
    model_evaluation_slice_v1,
    model_service_v1,
    operation_v1,
    pipeline_service_v1,
    pipeline_state_v1,
    prediction_service_v1,
    specialist_pool_v1,
    specialist_pool_service_v1,
    training_pipeline_v1,
    # v1beta1
    accelerator_type_v1beta1,
    annotation_v1beta1,
    annotation_spec_v1beta1,
    batch_prediction_job_v1beta1,
    completion_stats_v1beta1,
    custom_job_v1beta1,
    data_item_v1beta1,
    data_labeling_job_v1beta1,
    dataset_v1beta1,
    dataset_service_v1beta1,
    deployed_model_ref_v1beta1,
    encryption_spec_v1beta1,
    endpoint_v1beta1,
    endpoint_service_v1beta1,
    env_var_v1beta1,
    explanation_v1beta1,
    explanation_metadata_v1beta1,
    hyperparameter_tuning_job_v1beta1,
    io_v1beta1,
    job_service_v1beta1,
    job_state_v1beta1,
    machine_resources_v1beta1,
    manual_batch_tuning_parameters_v1beta1,
    model_v1beta1,
    model_evaluation_v1beta1,
    model_evaluation_slice_v1beta1,
    model_service_v1beta1,
    operation_v1beta1,
    pipeline_job_v1beta1,
    pipeline_service_v1beta1,
    pipeline_state_v1beta1,
    prediction_service_v1beta1,
    specialist_pool_v1beta1,
    specialist_pool_service_v1beta1,
    training_pipeline_v1beta1,
    metadata_service_v1beta1,
    tensorboard_v1beta1,
    tensorboard_service_v1beta1,
    tensorboard_data_v1beta1,
    tensorboard_experiment_v1beta1,
    tensorboard_run_v1beta1,
    tensorboard_service_v1beta1,
    tensorboard_time_series_v1beta1,
)
